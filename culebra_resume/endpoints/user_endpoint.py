from fastapi import APIRouter

api = APIRouter(prefix="/user")

@api.get("/")
async def list_users():
    return "List All Users"

