# 🛒 QR QuickShop

> Smart QR-Based Retail Management System — Browse, Cart, QR Checkout, and Worker Order Management.

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat-square)
![Flask](https://img.shields.io/badge/Flask-2.x-lightgrey?style=flat-square)
![SQLite](https://img.shields.io/badge/SQLite-3-003B57?style=flat-square)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-ORM-red?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=flat-square)

---

## 📌 About The Project

QR QuickShop is a full-stack retail management web application that digitizes the shopping experience.

Customers can browse products, manage a cart, save favourites, place online orders, and generate a QR code for offline pickup — all from the browser with no app required.

Workers get a real-time dashboard to view incoming orders and manage the full fulfilment lifecycle from placement to delivery.

> **Data persistence layer migrated from JSON → SQLite using SQLAlchemy ORM.**

---

## 📸 Screenshots

> Add screenshots of your running app here.

```
screenshots/
├── home.png          ← Customer product catalogue
├── cart.png          ← Cart management view
├── dashboard.png     ← Worker order dashboard
└── track.png         ← Order tracking page
```

*To add: Take screenshots of your running app → save in `screenshots/` folder → update this section with image links.*

---

## ✨ Features

### 👤 Customer Features
- Product catalogue browsing
- Product search
- Add to cart / remove products
- Quantity management
- Favourite products
- Move favourites → cart
- User registration and login
- Session management
- Online checkout
- QR code generation for offline pickup
- Real-time order tracking

### 🧑‍💼 Worker Features
- Worker authentication
- Worker dashboard
- View all placed orders
- Update order status: **Seen → Packed → Delivered**
- Auto-refresh order updates

### ⚙️ System Features
- SQLite database with SQLAlchemy ORM
- QR code generation (qrcode + Pillow)
- RESTful API design
- Persistent storage
- Responsive UI with Jinja2 templating

---

## 🛠 Tech Stack

| Layer      | Technology              |
|------------|-------------------------|
| Frontend   | HTML, CSS, JavaScript, Jinja2 |
| Backend    | Python, Flask           |
| Database   | SQLite, SQLAlchemy ORM  |
| Libraries  | qrcode, Pillow          |
| Tools      | VS Code, Git, GitHub    |

---

## 🏗 Architecture

```
Customer Browser
      ↓
Frontend (HTML / CSS / JS / Jinja2)
      ↓
Flask Backend (server.py)
      ↓
SQLAlchemy ORM (models.py)
      ↓
SQLite Database (database.db)
      ↓
Worker Dashboard (/dashboard)
```

---

## 📁 Project Structure

```
qr-quickshop/
│
├── backend/
│   ├── server.py              # Main Flask application
│   ├── models.py              # SQLAlchemy database models
│   │
│   ├── static/
│   │   ├── dashboard.js       # Worker dashboard scripts
│   │   ├── images/            # Product images
│   │   ├── qrcodes/           # Generated QR codes
│   │   └── styles/            # CSS stylesheets
│   │
│   └── templates/
│       ├── base.html
│       ├── index.html
│       ├── login.html
│       ├── favourites.html
│       ├── dashboard.html
│       ├── track.html
│       └── search.html
│
├── requirements.txt           # Python dependencies
├── README.md
└── screenshots/               # App screenshots
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.x
- pip

### Installation

**1. Clone the repository**
```bash
git clone https://github.com/yashwant-oruganti/qr-quickshop.git
cd qr-quickshop
```

**2. Create a virtual environment**
```bash
python -m venv .venv
```

**3. Activate the virtual environment**

Windows:
```bash
.venv\Scripts\activate
```

macOS / Linux:
```bash
source .venv/bin/activate
```

**4. Install all dependencies**
```bash
pip install -r requirements.txt
```

---

## ▶️ Run The Project

```bash
cd backend
python server.py
```

Open in your browser:

| Route | URL |
|---|---|
| Customer App | http://127.0.0.1:5000 |
| Worker Dashboard | http://127.0.0.1:5000/dashboard |

---

## 🗄 Database

**Engine:** SQLite
**File:** `backend/database.db`

### Tables

**User**
```
id | name | email | mobile | password | role
```

**Order**
```
id | order_uid | user_id | items | total | status
```

**Favourite**
```
id | user_id | item_name | price | img
```

---

## 🔗 API Endpoints

### Products
```http
GET /items
```

### Search
```http
GET /search?q=<query>
```

### Cart
```http
GET  /cart
POST /add_to_cart
POST /update_cart
```

### Favourites
```http
GET  /favourites/data
POST /add_favourite
POST /remove_favourite
POST /move_to_cart
```

### Orders
```http
POST /checkout
GET  /orders
POST /update_order
GET  /track/<order_id>
```

### Authentication
```http
GET  /login
POST /auth
GET  /logout
```

---

## 📦 Order Workflow

```
Customer places order
        ↓
  Order Created
        ↓
Worker Dashboard (Incoming)
        ↓
     Seen ✅
        ↓
    Packed 📦
        ↓
  Delivered 🚚
        ↓
Customer tracks via /track/<order_id>
```

---

## 🔮 Future Enhancements

- [ ] Payment gateway integration
- [ ] Barcode scanner support
- [ ] Inventory management module
- [ ] Push notifications
- [ ] Analytics dashboard
- [ ] AI-based product recommendations
- [ ] Multi-store support
- [ ] Docker containerization
- [ ] Cloud deployment (Railway / Render)
- [ ] PostgreSQL migration

---

## 👤 Author

**Yashwant Kumar Oruganti**
B.Tech — Electronics and Communication Engineering
Dr. Lankapalli Bullayya College of Engineering, Visakhapatnam

[![GitHub](https://img.shields.io/badge/GitHub-yashwant--oruganti-181717?style=flat-square&logo=github)](https://github.com/yashwant-oruganti)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0077B5?style=flat-square&logo=linkedin)](https://www.linkedin.com/in/oruganti-yashwant-kumar-271617296/)

📧 orugantiyashwantkumar@gmail.com

---

