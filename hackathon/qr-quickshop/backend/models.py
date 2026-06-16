from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# ---------------- Models ----------------
class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(120), unique=True, nullable=False)
    mobile = db.Column(db.String(15))
    password = db.Column(db.String(100))
    role = db.Column(db.String(20), default="customer")

class Favourite(db.Model):
    __tablename__ = "favourites"
    id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.String(100))
    price = db.Column(db.Float)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    user = db.relationship("User", backref=db.backref("favourites", lazy=True))

class Order(db.Model):
    __tablename__ = "orders"
    id = db.Column(db.Integer, primary_key=True)
    order_uid = db.Column(db.String(20), unique=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    items = db.Column(db.Text)  # JSON string of cart items
    total = db.Column(db.Float)
    status = db.Column(db.String(20), default="Pending")
    user = db.relationship("User", backref=db.backref("orders", lazy=True))

# ---------------- Create DB ----------------
if __name__ == "__main__":
    # Use app context so SQLAlchemy knows which app to bind to
    with app.app_context():
        db.create_all()
        print("✅ database.db created with all tables!")
