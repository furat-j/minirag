from fastapi import FastAPI, APIRouter

base_router = APIRouter()

@base_router.get("/")
async def welcome():
    return {
        "message": "Hello ALL!"
    }

