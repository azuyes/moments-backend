from fastapi import APIRouter
from app.api.routes import ai,login

api_router = APIRouter()

api_router.include_router(ai.router, prefix="/ai", tags=["AI"])
api_router.include_router(login.router, prefix="/login", tags=["登录"])
