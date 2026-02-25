from app.schemas.developer_schems import Developerprofile
from app.services.developer_service import create_profile,get_all_developers
from app.utils import get_current_user
from fastapi import FastAPI,APIRouter,Depends
router=APIRouter()

@router.post("/create-profile")
async def createdevprofile(profile:Developerprofile,current_user:dict=Depends(get_current_user)):
    user_id=str(current_user["_id"])
    profile_id=await create_profile(user_id,profile)

    return{
        "message":"Developer profile created successfully",
        "profile_id":profile_id
    }
@router.get("/developers")
async def view_all_developers(current_user:dict=Depends(get_current_user)):
    developers=await get_all_developers()
    return developers