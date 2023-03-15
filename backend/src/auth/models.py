from fastapi_users.db import SQLAlchemyBaseUserTableUUID

from sqlalchemy import Column, String
from src.database import Base


class User(SQLAlchemyBaseUserTableUUID, Base):
    __tablename__ = "users"
    """
    Fields inherited from SQLAlchemyBaseUserTableUUID:
    - id: UUID
    - email: str
    - hashed_password: str
    - is_active: bool
    - is_superuser: bool
    """

    username = Column(String)
