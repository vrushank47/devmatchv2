DevMatch v2 – Developer Profile Management API

DevMatch v2 is a RESTful backend API designed to manage developer profiles with secure user authentication and protected access to resources.

The application enables users to register, authenticate, create and manage their developer profiles, and discover other developers through skill-based information stored in a MongoDB database.

This project demonstrates backend application development using modern API design principles, JWT-based authentication, and NoSQL database integration.

Key Features

User Registration and Authentication

Secure Password Hashing using Bcrypt

JWT-based Authorization

Protected API Routes

Create and Update Developer Profiles

View Developer Profiles

One-to-One Mapping between User Accounts and Developer Profiles

MongoDB Integration for Persistent Data Storage

Technology Stack

Python

FastAPI

MongoDB

PyMongo

JSON Web Tokens (JWT)

Bcrypt

Uvicorn

Project Structure
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
Installation & Setup
1. Clone the Repository
git clone https://github.com/YOUR_USERNAME/devmatchv2.git
cd devmatchv2
2. Create a Virtual Environment
python -m venv venv
source venv/bin/activate
3. Install Dependencies
pip install -r requirements.txt
4. Configure Environment Variables

Create a .env file in the root directory:

MONGO_URI=mongodb://localhost:27017
DATABASE_NAME=devmatch
SECRET_KEY=your_secret_key
ALGORITHM=HS256
5. Run the Application
uvicorn app.main:app --reload

Access interactive API documentation at:

http://127.0.0.1:8000/docs
Authentication Workflow

Register a new user via /signup

Log in using /login

Obtain JWT access token

Authorize API requests using:

Bearer <access_token>

Access protected endpoints such as:

/create-profile

/developers

Database Schema
Users Collection

email

password (hashed)

Developers Collection

user_id

name

bio

skills

experience_level

Each registered user is associated with a single developer profile.

Author

Vrushank Saravade

