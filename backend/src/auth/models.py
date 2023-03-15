from fastapi_users.db import SQLAlchemyBaseUserTableUUID

from sqlalchemy import Column, String
from src.database import Base


class User(SQLAlchemyBaseUserTableUUID, Base):
    __tablename__ = "users"

    username = Column(String)
