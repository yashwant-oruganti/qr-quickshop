// 🔹 Fetch and display all orders
async function loadOrders() {
  const container = document.getElementById("ordersContainer");
  container.innerHTML = "<p>⏳ Loading orders...</p>";

  try {
    // ✅ Use unified endpoint that works for both dashboards
    const res = await fetch("/orders/data");
    const orders = await res.json();

    container.innerHTML = ""; // clear old content

    if (!orders || orders.length === 0) {
      container.innerHTML = "<p>No orders found 🛒</p>";
      return;
    }

    // 🔹 Render each order card
    orders.forEach(order => {
      const div = document.createElement("div");
      div.className = "order-card";

      // 🧾 Build item list
      const itemsList = order.items
        .map(
          i =>
            `<li>${i.name} - ₹${i.price} × ${i.quantity} = ₹${
              i.price * i.quantity
            }</li>`
        )
        .join("");

      // 🟢 Different views for MART and CUSTOMER dashboards
      const isMart = window.location.pathname.includes("mart");

      div.innerHTML = `
        <h3>Order ID: ${order.id}</h3>
        <p><strong>Status:</strong> 
          <span class="status ${order.status.toLowerCase()}">${order.status}</span>
        </p>
        <ul>${itemsList}</ul>
        <p><strong>Total:</strong> ₹${order.total}</p>
        ${
          isMart
            ? `
          <div class="actions">
            <button class="pending" onclick="updateOrder('${order.id}', 'Pending')">⏳ Pending</button>
            <button class="packed" onclick="updateOrder('${order.id}', 'Packed')">📦 Packed</button>
            <button class="delivered" onclick="updateOrder('${order.id}', 'Delivered')">✅ Delivered</button>
          </div>`
            : ""
        }
      `;

      container.appendChild(div);
    });
  } catch (err) {
    console.error("Error loading orders:", err);
    container.innerHTML =
      "<p style='color:red;'>⚠️ Failed to load orders. Try again later.</p>";
  }
}

// 🔹 Update order status (only for MART dashboard)
async function updateOrder(id, status) {
  try {
    const res = await fetch("/update_order", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ id, status })
    });

    const data = await res.json();
    if (data.success) {
      console.log(`✅ Order ${id} updated to ${status}`);
      loadOrders();
    } else {
      alert("⚠️ Failed to update order: " + data.message);
    }
  } catch (err) {
    console.error("Error updating order:", err);
    alert("Failed to update order status!");
  }
}

// 🔄 Auto-refresh every 10 seconds
setInterval(loadOrders, 10000);

// 🧹 Clear dashboard every 10 minutes
setInterval(() => {
  const container = document.getElementById("ordersContainer");
  if (container) {
    container.innerHTML =
      "<p>⏳ Dashboard cleared automatically. Waiting for new orders...</p>";
  }
}, 10 * 60 * 1000); // 600000 ms

// 🚀 Load orders on page ready
document.addEventListener("DOMContentLoaded", loadOrders);
