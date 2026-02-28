# 🚀 DevMatch v2 – Secure Developer Networking Backend

DevMatch v2 is a secure and scalable RESTful backend built to power developer networking platforms, collaboration systems, and recruitment solutions.

The platform enables users to register, authenticate securely, create professional developer profiles, and explore other developers based on skills and experience — all backed by MongoDB and JWT-based authentication.

This project reflects production-oriented backend architecture using modern API standards, secure authentication mechanisms, and clean modular design.

---

## ✨ Core Features

✔️ Secure User Registration & Login
✔️ Password Hashing with Bcrypt
✔️ JWT-Based Authentication & Authorization
✔️ Protected API Endpoints
✔️ Create & Manage Developer Profiles
✔️ Retrieve Developer Profiles (Authenticated Access)
✔️ One-to-One Mapping Between Users and Developer Profiles
✔️ MongoDB Persistent Storage
✔️ Interactive Swagger Documentation

---

## 🛠️ Technology Stack

| Technology | Role                           |
| ---------- | ------------------------------ |
| Python     | Core Programming Language      |
| FastAPI    | High-Performance API Framework |
| MongoDB    | NoSQL Database                 |
| PyMongo    | MongoDB Driver                 |
| JWT        | Secure Authentication          |
| Bcrypt     | Password Hashing               |
| Uvicorn    | ASGI Server                    |

---

## 📁 Project Architecture

devmatchv2/

│
├── app/
│   ├── core/
│   │   └── config.py
│   ├── routes/
│   │   ├── auth_routes.py
│   │   └── developer_routes.py
│   ├── schemas/
│   │   ├── user_schema.py
│   │   └── developer_schema.py
│   ├── services/
│   │   ├── auth_service.py
│   │   └── developer_service.py
│   ├── db.py
│   ├── utils.py
│   └── main.py
│
├── .env
├── requirements.txt
└── README.md

---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository

git clone https://github.com/YOUR_USERNAME/devmatchv2.git
cd devmatchv2

---

### 2️⃣ Create Virtual Environment

python -m venv venv
source venv/bin/activate

---

### 3️⃣ Install Dependencies

pip install -r requirements.txt

---

### 4️⃣ Configure Environment Variables

Create a `.env` file in the root directory:

MONGO_URI=mongodb://localhost:27017
DATABASE_NAME=devmatch
SECRET_KEY=your_secret_key
ALGORITHM=HS256

---

### 5️⃣ Run the Server

uvicorn app.main:app --reload

---

## 📌 API Documentation

After starting the server, visit:

http://127.0.0.1:8000/docs

Swagger UI allows interactive testing of all endpoints.

---

## 🔐 Authentication Flow

1. Register using `/signup`
2. Login via `/login`
3. Receive JWT Access Token
4. Authorize requests using:

Bearer <access_token>

5. Access protected endpoints such as:

• `/create-profile`
• `/developers`

---

## 🗄️ Database Design

### Users Collection

• email
• password (hashed)

### Developers Collection

• user_id
• name
• bio
• skills
• experience_level

Each user account is linked to exactly one developer profile.

---

## 🎯 Intended Use Cases

• Developer Networking Platforms
• Hiring & Recruitment Backends
• Skill Discovery Systems
• Collaboration Platforms
• Portfolio Aggregation Services

---

## 👨‍💻 Author

Vrushank Saravade

---



Built with performance, security, and scalability in mind.
