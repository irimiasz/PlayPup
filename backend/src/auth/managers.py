from logging import getLogger
from typing import Optional
import uuid

from fastapi import Depends, Request
from fastapi_users import BaseUserManager, UUIDIDMixin


from .config import get_user_db
from .models import User

logger = getLogger(__name__)


class UserManager(UUIDIDMixin, BaseUserManager[User, uuid.UUID]):
    async def on_after_register(
        self, user: User, request: Optional[Request] = None
    ) -> None:
        logger.info("User %s has successfully registered", user.id)


async def get_user_manager(user_db=Depends(get_user_db)):
    yield UserManager(user_db)
