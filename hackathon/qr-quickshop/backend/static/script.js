// ============================
// Load Items from server
// ============================
async function loadItems() {
  let res = await fetch("/items");
  let items = await res.json();
  let container = document.getElementById("itemsContainer");
  container.innerHTML = "";

  items.forEach(item => {
    let card = document.createElement("div");
    card.style.border = "1px solid #ccc";
    card.style.padding = "10px";
    card.style.borderRadius = "10px";
    card.style.textAlign = "center";
    card.style.boxShadow = "2px 2px 5px rgba(0,0,0,0.1)";

    card.innerHTML = `
      <img src="${item.img}" alt="${item.name}" width="100"><br>
      <strong>${item.name}</strong><br>
      Price: ₹${item.price}<br>
      <button onclick="addToCart('${item.name}')">Add to Cart</button>
    `;
    container.appendChild(card);
  });
}

// ============================
// Add Item to Cart
// ============================
async function addToCart(itemName = null) {
  let item = itemName || document.getElementById("itemInput").value;
  if (item.trim() === "") return alert("Enter an item!");

  let res = await fetch("/add_to_cart", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ item })
  });
  let data = await res.json();
  alert(data.message);

  if (!itemName) document.getElementById("itemInput").value = "";
  viewCart();
}

// ============================
// View Cart
// ============================
async function viewCart() {
  let res = await fetch("/cart");
  let data = await res.json();
  let cartList = document.getElementById("cartList");
  let cartTotal = document.getElementById("cartTotal");
  cartList.innerHTML = "";

  data.cart.forEach(item => {
    let li = document.createElement("li");
    li.innerHTML = `
      ${item.name} - ₹${item.price} × ${item.quantity} = ₹${item.subtotal}
      <button onclick="updateCart('${item.name}', 'dec')">-</button>
      <button onclick="updateCart('${item.name}', 'inc')">+</button>
      <button onclick="updateCart('${item.name}', 'remove')">❌</button>
    `;
    cartList.appendChild(li);
  });

  cartTotal.innerHTML = "<strong>Total: ₹" + data.total + "</strong>";
}

// ============================
// Update Cart
// ============================
async function updateCart(item, action) {
  let res = await fetch("/update_cart", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ item, action })
  });
  await res.json();
  viewCart();
}

// ============================
// Checkout (Online / Offline)
// ============================
async function checkout(mode) {
  let res = await fetch("/checkout", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ mode })
  });
  let data = await res.json();

  let msgBox = document.getElementById("checkoutMsg");
  msgBox.innerHTML = `<p>${data.message}</p>`;

  // For offline orders -> QR code
  if (data.qr_url) {
    msgBox.innerHTML += `
      <a href="${data.qr_url}" download="checkout_qr.png">
        <button style="margin-top:10px;">Download QR Code</button>
      </a>
    `;
  }

  // For online orders -> show status tracker
  if (data.message.includes("Order ID")) {
    let orderId = data.message.split(": ")[1];
    msgBox.innerHTML += `
      <p>📦 Track your order status below:</p>
      <button onclick="checkOrderStatus('${orderId}')">Check Status</button>
      <p id="orderStatus_${orderId}"></p>
    `;
  }

  viewCart();
}

// ============================
// Check Order Status
// ============================
async function checkOrderStatus(orderId) {
  let res = await fetch("/orders");
  let orders = await res.json();
  let order = orders.find(o => o.id === orderId);

  let statusBox = document.getElementById(`orderStatus_${orderId}`);
  if (order) {
    statusBox.innerHTML = `✅ Current Status: <strong>${order.status}</strong>`;
  } else {
    statusBox.innerHTML = "❌ Order not found!";
  }
}

// ============================
// Run on Page Load
// ============================
document.addEventListener("DOMContentLoaded", () => {
  loadItems();
  viewCart();
});
