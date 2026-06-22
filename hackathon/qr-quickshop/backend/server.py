from flask import Flask, render_template, abort, request, jsonify, url_for, redirect, session
from models import db, User, Order, Favourite
import qrcode, json, uuid, os, socket

app = Flask(__name__)
app.secret_key = "supersecretkey"

# ----------------------------
# Database Configuration
# ----------------------------
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)
with app.app_context():
    db.create_all()

# ----------------------------
# Store Items (Sample)
# ----------------------------
store_items = [
    {"id": 1, "name": "Apple", "price": 10, "img": "/static/images/apple.webp"},
    {"id": 2, "name": "Banana", "price": 5, "img": "/static/images/banana.png"},
    {"id": 3, "name": "Milk", "price": 30, "img": "/static/images/milk.webp"},
    {"id": 4, "name": "Bread", "price": 25, "img": "/static/images/bread.webp"},
]

cart = {}

# ----------------------------
# Home
# ----------------------------
@app.route("/")
def home():
    return render_template("index.html")

# ----------------------------
#REST END POINT (PRODUCTS)
# ----------------------------
@app.route("/api/products", methods=["GET"])
def get_products():
    return jsonify({
	"success": True,
	"count":len(store_items), 
	"products": store_items})

# ----------------------------
# Search
# ----------------------------
@app.route("/search")
def search():
    query = request.args.get("q", "").lower().strip()
    if not query:
        return redirect(url_for("home"))
    results = [item for item in store_items if query in item["name"].lower()]
    message = f"Showing results for '{query}':" if results else f"No products found for '{query}'."
    return render_template("search.html", results=results, message=message)

# ----------------------------
# Favourites
# ----------------------------
@app.route("/favourites")
def favourites_page():
    return render_template("favourites.html")


@app.route("/favourites/data")
def get_favourites():
    if "user" not in session:
        return jsonify([])
    user_id = session["user"]["id"]
    favs = Favourite.query.filter_by(user_id=user_id).all()
    return jsonify([
        {"name": f.item_name, "price": f.price, "img": f.img}
        for f in favs
    ])


@app.route("/add_favourite", methods=["POST"])
def add_favourite():
    if "user" not in session:
        return jsonify({"error": "Login required"}), 401

    data = request.json
    product_id = data.get("product_id")
    product = next((i for i in store_items if i["id"] == product_id), None)
    if not product:
        return jsonify({"message": "Item not found!"}), 400

    # Prevent duplicates
    existing = Favourite.query.filter_by(
        user_id=session["user"]["id"], item_name=product["name"]
    ).first()
    if existing:
        return jsonify({"message": "Already in favourites!"})

    new_fav = Favourite(
        user_id=session["user"]["id"],
        item_name=product["name"],
        price=product["price"],
        img=product["img"]
    )
    db.session.add(new_fav)
    db.session.commit()
    return jsonify({"message": "Added to favourites!"})


@app.route("/remove_favourite", methods=["POST"])
def remove_favourite():
    if "user" not in session:
        return jsonify({"error": "Login required"}), 401
    data = request.get_json()
    item_name = data.get("item")
    user_id = session["user"]["id"]
    fav = Favourite.query.filter_by(item_name=item_name, user_id=user_id).first()
    if fav:
        db.session.delete(fav)
        db.session.commit()
        return jsonify({"message": f"{item_name} removed!"})
    return jsonify({"message": "Item not found!"}), 404

# ----------------------------
# Cart
# ----------------------------
@app.route("/cart")
def get_cart():
    cart_items, total = [], 0
    for name, info in cart.items():
        subtotal = info["price"] * info["quantity"]
        total += subtotal
        cart_items.append({
            "name": name,
            "price": info["price"],
            "quantity": info["quantity"],
            "subtotal": subtotal
        })
    return jsonify({"cart": cart_items, "total": total})


@app.route("/add_to_cart", methods=["POST"])
def add_to_cart():
    data = request.json
    item_name = data.get("item")
    item = next((i for i in store_items if i["name"].lower() == item_name.lower()), None)
    if not item:
        return jsonify({"message": "Item not found!"}), 400
    if item_name in cart:
        cart[item_name]["quantity"] += 1
    else:
        cart[item_name] = {"price": item["price"], "quantity": 1}
    return jsonify({"message": f"{item_name} added to cart!"})


@app.route("/update_cart", methods=["POST"])
def update_cart():
    data = request.json
    item_name, action = data.get("item"), data.get("action")
    if item_name not in cart:
        return jsonify({"message": "Item not in cart!"}), 400
    if action == "inc":
        cart[item_name]["quantity"] += 1
    elif action == "dec":
        cart[item_name]["quantity"] -= 1
        if cart[item_name]["quantity"] <= 0:
            del cart[item_name]
    elif action == "remove":
        del cart[item_name]
    return jsonify({"message": f"Cart updated: {action} {item_name}"})

# ----------------------------
# Checkout
# ----------------------------
@app.route("/checkout", methods=["POST"])
def checkout():
    global cart
    if not cart:
        return jsonify({"message": "Cart is empty!"})

    data = request.json
    mode = data.get("mode", "offline")
    user_id = session.get("user", {}).get("id")

    cart_items = [
        {
            "name": name,
            "price": info["price"],
            "quantity": info["quantity"],
            "subtotal": info["price"] * info["quantity"]
        } for name, info in cart.items()
    ]
    total = sum(item["subtotal"] for item in cart_items)

    order_uid = str(uuid.uuid4())[:8]
    new_order = Order(
        order_uid=order_uid,
        user_id=user_id,
        items=json.dumps(cart_items),
        total=total,
        status="Pending"
    )
    db.session.add(new_order)
    db.session.commit()
    cart.clear()

    if mode == "online":
        return jsonify({
            "message": f"✅ Online order placed successfully!",
            "track_url": url_for("track_order", order_id=order_uid)
        })
    else:
        qr_data = f"Order Total: ₹{total}\n" + "\n".join(
            [f"{i['name']} x{i['quantity']} = ₹{i['subtotal']}" for i in cart_items]
        )
        qr = qrcode.make(qr_data)
        qr_folder = os.path.join(app.static_folder, "qrcodes")
        os.makedirs(qr_folder, exist_ok=True)
        qr_filename = f"checkout_{order_uid}.png"
        qr_path = os.path.join(qr_folder, qr_filename)
        qr.save(qr_path)
        return jsonify({
            "message": "🛍️ Offline checkout successful!",
            "qr_url": url_for("static", filename=f"qrcodes/{qr_filename}")
        })

# ----------------------------
# Worker Dashboard
# ----------------------------
@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


@app.route("/orders")
def get_orders():
    orders = Order.query.all()
    order_list = [{
        "id": o.order_uid,
        "items": json.loads(o.items),
        "total": o.total,
        "status": o.status,
        "user": User.query.get(o.user_id).name if o.user_id else "Guest",
    } for o in orders]
    return jsonify(order_list)


@app.route("/update_order", methods=["POST"])
def update_order():
    data = request.json
    order_id, new_status = data.get("id"), data.get("status")
    order = Order.query.filter_by(order_uid=order_id).first()
    if not order:
        return jsonify({"message": "Order not found!"}), 404
    order.status = new_status
    db.session.commit()
    return jsonify({"message": f"Order {order_id} updated to {new_status}"})

# ----------------------------
# Track Order
# ----------------------------
# Example function to get order
def get_order(order_id):
    # Replace this with your actual DB query
    orders = {
        "2d87299e": {
            "order_uid": "2d87299e",
            "status": "Processing",
            "items": '[{"name": "Apple", "quantity": 2, "subtotal": 200}, {"name": "Banana", "quantity": 5, "subtotal": 100}]',
            "total": 300
        }
    }
    return orders.get(order_id)

@app.route("/track/<order_id>")
def track_order(order_id):
    order = get_order(order_id)
    if not order:
        abort(404, "Order not found")

    # Convert items from JSON string to Python list
    order_items = json.loads(order['items'])

    return render_template(
        "track.html",
        order=order,
        items=order_items,   # pass Python list
        delivered=(order['status'] == "Delivered"),
        order_id=order_id
    )

# ----------------------------
# Authentication
# ----------------------------
@app.route("/login")
def login_page():
    return render_template("login.html")


@app.route("/auth", methods=["POST"])
def auth():
    data = request.get_json()
    name, email, mobile, password, role = (
        data.get("name"),
        data.get("email"),
        data.get("mobile"),
        data.get("password"),
        data.get("role", "customer"),
    )
    user = User.query.filter_by(email=email).first()
    if user:
        if user.password != password:
            return jsonify({"message": "❌ Invalid password!"})
        session["user"] = {"id": user.id, "name": user.name, "email": user.email, "role": user.role}
        message, redirect_url = "✅ Login successful!", (
            url_for("dashboard") if user.role == "worker" else url_for("home")
        )
    else:
        new_user = User(name=name, email=email, mobile=mobile, password=password, role=role)
        db.session.add(new_user)
        db.session.commit()
        session["user"] = {"id": new_user.id, "name": name, "email": email, "role": role}
        message, redirect_url = "🎉 Registration successful!", (
            url_for("dashboard") if role == "worker" else url_for("home")
        )
    return jsonify({"message": message, "redirect": redirect_url})


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("home"))

# ----------------------------
# Run App
# ----------------------------
if __name__ == "__main__":
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        local_ip = s.getsockname()[0]
    except Exception:
        local_ip = "127.0.0.1"
    finally:
        s.close()

    print("\n" + "=" * 60)
    print(" 🚀 QR QuickShop is running with SQLite DB! ")
    print(f" • PC: http://127.0.0.1:5000")
    print(f" • Phone (same Wi-Fi): http://{local_ip}:5000")
    print(f" • Worker Dashboard: http://127.0.0.1:5000/dashboard")
    print("=" * 60 + "\n")

    app.run(host="0.0.0.0", port=5000, debug=True)
