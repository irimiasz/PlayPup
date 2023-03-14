from fastapi import APIRouter

from .auth.routers import router as auth_router


api_router = APIRouter(prefix="/api")
api_router.include_router(auth_router)
