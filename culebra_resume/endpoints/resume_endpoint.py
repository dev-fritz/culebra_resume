from fastapi import APIRouter

api = APIRouter(prefix="/resume")

@api.get("/")
async def list_resume():
    return "List All Resumes"

