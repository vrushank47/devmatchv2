# 🚀 DevMatch v2 – Developer Profile Management API

DevMatch v2 is a secure, scalable RESTful backend API built to manage developer profiles with robust authentication and protected resource access.

The application enables users to register, authenticate, create and manage their developer profiles, and discover other developers through skill-based information stored in a MongoDB database.

This project demonstrates real-world backend development using modern API design principles, JWT-based authentication, and NoSQL database integration.

---

## ✨ Key Features

✔️ User Registration and Login
✔️ Secure Password Hashing using Bcrypt
✔️ JWT-based Authentication & Authorization
✔️ Protected API Routes
✔️ Create Developer Profiles
✔️ View All Developer Profiles
✔️ One-to-One Mapping between Users and Developer Profiles
✔️ MongoDB Integration for Persistent Data Storage
✔️ Interactive Swagger API Documentation

---

## 🛠️ Technology Stack

| Technology | Purpose                   |
| ---------- | ------------------------- |
| Python     | Core Programming Language |
| FastAPI    | Backend API Framework     |
| MongoDB    | NoSQL Database            |
| PyMongo    | Database Connector        |
| JWT        | Authentication            |
| Bcrypt     | Password Hashing          |
| Uvicorn    | ASGI Server               |

---

## 📁 Project Structure

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

### 1️⃣ Clone the Repository

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

### 5️⃣ Run the Application

uvicorn app.main:app --reload

---

## 📌 Access API Documentation

After running the server, open:

http://127.0.0.1:8000/docs

Swagger UI provides an interactive interface to test all API endpoints.

---

## 🔐 Authentication Workflow

1. Register a new user via `/signup`
2. Login using `/login`
3. Obtain JWT Access Token
4. Authorize API Requests using:

Bearer <access_token>

5. Access Protected Endpoints:

• `/create-profile`
• `/developers`

---

## 🗄️ Database Schema

### Users Collection

• email
• password (hashed)

### Developers Collection

• user_id
• name
• bio
• skills
• experience_level

Each registered user is associated with a single developer profile.

---

## 👨‍💻 Author

**Vrushank Saravade**

---




