from fastapi import FastAPI
from app.db import connect_to_mongo,close_mongo_connection
from app.routes.auth_routes import router as auth_router
from app.routes import developer_routes 


app=FastAPI()




@app.on_event("startup")
def startup_db_client():
    connect_to_mongo()
@app.on_event("shutdown")
def shutdown_db_client():
    close_mongo_connection()
app.include_router(auth_router)
app.include_router(developer_routes.router)
@app.get("/")
def root():
    return {"message":"devmatch API running"}