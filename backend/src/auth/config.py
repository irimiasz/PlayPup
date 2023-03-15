import os

from fastapi import Depends
from fastapi_users.db import SQLAlchemyUserDatabase
from fastapi_users.authentication import (
    AuthenticationBackend,
    CookieTransport,
    JWTStrategy,
)
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_session

from .constants import COOKIE_MAX_AGE
from .models import User


secret = os.getenv("APP_SECRET")
cookie_transport = CookieTransport(cookie_max_age=COOKIE_MAX_AGE)


def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=secret, lifetime_seconds=COOKIE_MAX_AGE)


auth_backend = AuthenticationBackend(
    name="jwt", transport=cookie_transport, get_strategy=get_jwt_strategy
)


async def get_user_db(session: AsyncSession = Depends(get_session)):
    yield SQLAlchemyUserDatabase(session, User)
