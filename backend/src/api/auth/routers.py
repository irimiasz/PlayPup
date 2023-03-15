import uuid

from fastapi import APIRouter

from fastapi_users import FastAPIUsers

from src.auth.config import auth_backend
from src.auth.managers import get_user_manager
from src.auth.models import User
from src.auth.schemas import UserCreate, UserRead

users = FastAPIUsers[User, uuid.UUID](get_user_manager, [auth_backend])

router = APIRouter(prefix="/auth")
router.include_router(users.get_register_router(UserRead, UserCreate))
