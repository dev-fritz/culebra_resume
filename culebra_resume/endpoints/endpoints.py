from fastapi import APIRouter
from culebra_resume.endpoints.user_endpoint import api as user_api
from culebra_resume.endpoints.resume_endpoint import api as resume_api

include_routes = APIRouter(prefix="/api/v1")

include_routes.include_router(resume_api)
include_routes.include_router(user_api)
