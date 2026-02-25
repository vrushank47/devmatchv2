from app.db import db_instance
from app.core.security import hash_password, verify_password,create_access_token

def register_user(user_data):
    user_collection=db_instance.db["users"]

    existing_users=user_collection.find_one({"email":user_data.email})
    if existing_users:
        return {"error":"user already exist"}
    hashed_password=hash_password(user_data.password)

    user={
        "email": user_data.email,
        "password":hashed_password
    }
    user_collection.insert_one(user)
    return {"message": "user registered successfully"}

def login_user(user_data):
    user_collection=db_instance.db["users"]
    user=user_collection.find_one({"email":user_data.email})
    if not user:
        return {"message":"invalid password or email"}
    if not verify_password(user_data.password , user["password"]):
        return {"message": "invalid email or password"}
    
    token= create_access_token(
        {"user_id":str(user["_id"])}
    )
    return {"access_token": token}