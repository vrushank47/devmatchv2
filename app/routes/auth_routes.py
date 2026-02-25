from fastapi import APIRouter
from app.schemas.user_schema import userlogin,userregister
from app.services.auth_service import register_user,login_user

router=APIRouter()
@router.post("/register")
def register(user:userregister):
    return register_user(user)
@router.post("/login")
def login(user:userlogin):
    return login_user(user)
    