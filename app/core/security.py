from passlib.context import CryptContext
from jose import jwt 
from datetime import timedelta,datetime
from app.core.config import settings

pwd_context=CryptContext(schemes=["bcrypt"],deprecated="auto")


def hash_password(password:str)->str:
    if len(password.encode("utf-8"))>72:
        raise ValueError("password too long")
    return pwd_context.hash(password)

def verify_password(plain_password:str , hashed_password:str)->bool:
    return pwd_context.verify(plain_password,hashed_password)


def create_access_token(data:dict):
    to_encode=data.copy()
    expire_time = datetime.utcnow()+timedelta(
        minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
    )
    to_encode.update({"exp":expire_time})

    encoded_jwt=jwt.encode(
        to_encode,
        settings.SECRET_KEY,
        algorithm=settings.ALGORITHM
    )
    return encoded_jwt