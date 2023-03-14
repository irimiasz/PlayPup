import re
from pydantic import BaseModel, EmailStr, validator

from .constants import MINIMUM_USERNAME_LENGTH, STRONG_PASSOWRD_REGEX


class UserCreateModel(BaseModel):
    username: str
    email: EmailStr
    password: str

    @validator("username")
    def validate_username(cls, v):
        if len(v) < MINIMUM_USERNAME_LENGTH:
            raise ValueError("Username must be at least 5 characters.")
        if v[0].isnumeric():
            raise ValueError("Username cannot start with a number.")
        return v

    @validator("password")
    def validate_password(cls, v):
        if not re.match(STRONG_PASSOWRD_REGEX, v):
            raise ValueError(
                "Password is not strong enough. It should have minimum 8 signs, at least one capital letter, "
                "number and special character"
            )
