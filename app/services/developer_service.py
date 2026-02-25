from app.db import get_developer_collection

async def create_profile(user_id,profile_data):
    developer_collection=get_developer_collection()
    existing_profile=developer_collection.find_one({
        "user_id":user_id
    })


    profile=profile_data.dict()
    profile["user_id"]=user_id
    if existing_profile:
        developer_collection.update_one(
            {"user_id":user_id},
            {"$set":profile}
        )
        return "profile updated"

    else:
        result=developer_collection.insert_one(profile)
        return str(result.inserted_id)
async def get_all_developers():
    developer_collection=get_developer_collection()
    developers=developer_collection.find()
    dev_list=[]
    for dev in developers:
        dev["_id"]=str(dev["_id"])
        dev_list.append(developers)
    return dev_list