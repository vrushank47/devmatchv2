from pydantic import EmailStr,BaseModel
from typing import Literal

class Developerprofile(BaseModel):
    name:str
    bio:str
    skills:list[str]
    experience:str
    