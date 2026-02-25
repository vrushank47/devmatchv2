from fastapi import HTTPException,Depends,status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import JWTError,jwt
from app.db import get_user_collection
from app.core.config import settings
from bson import ObjectId

security=HTTPBearer()

def get_current_user(
        credentials:HTTPAuthorizationCredentials=Depends(security)
):
    token=credentials.credentials
    try:
        payload=jwt.decode(
            token,
            settings.SECRET_KEY,
            algorithms=[settings.ALGORITHM]
        )
        user_id=payload.get("user_id")

        if user_id is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="invalid token")
        user_collection=get_user_collection()
        user=user_collection.find_one(
            
            {"_id":ObjectId(user_id)}
        )
        if user is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="user not found"
        
        )
        return user
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="token is invalid or expired"
        )