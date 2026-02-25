from app.core.config import settings
from pymongo import MongoClient

class Database:
    client:MongoClient=None
    db=None

db_instance=Database()
def connect_to_mongo():
    db_instance.client=MongoClient(settings.MONGO_URI)
    db_instance.db=db_instance.client[settings.DATABASE_NAME]
    print("connected to mongodb")
def close_mongo_connection():
    if db_instance.client:
        db_instance.client.close()
        print("mongodb connection closed")
def get_user_collection():
    return db_instance.db["users"]
def get_developer_collection():
    return db_instance.db["developers"]
