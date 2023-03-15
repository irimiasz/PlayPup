import re
import uuid

from fastapi_users import schemas

from pydantic import validator

from .constants import (
    MINIMUM_USERNAME_LENGTH,
    STRONG_PASSWORD_REGEX,
    MESSAGE_PASSWORD_TOO_WEAK,
    MESSAGE_USERNAME_STARTS_WITH_NUMBER,
    MESSAGE_USERNAME_TOO_SHORT,
)


class UserRead(schemas.BaseUser[uuid.UUID]):
    username: str


class UserCreate(schemas.BaseUserCreate):
    username: str

    @validator("username")
    def validate_username(cls, v):
        if len(v) < MINIMUM_USERNAME_LENGTH:
            raise ValueError(MESSAGE_USERNAME_TOO_SHORT)
        if v[0].isnumeric():
            raise ValueError(MESSAGE_USERNAME_STARTS_WITH_NUMBER)
        return v

    @validator("password")
    def validate_strong_password(cls, v):
        if not re.match(STRONG_PASSWORD_REGEX, v):
            raise ValueError(MESSAGE_PASSWORD_TOO_WEAK)
        return v
