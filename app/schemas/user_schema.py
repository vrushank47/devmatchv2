from pydantic import BaseModel, EmailStr, Field


class userregister(BaseModel):
    email:EmailStr
    password:str=Field(...,min_length=8,max_length=64)

class userlogin(BaseModel):
    email:EmailStr
    password:str=Field(
        ...,
        min_length=8,
        max_length=64
        
    )


