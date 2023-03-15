from typing import AsyncGenerator

import os

from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession, create_async_engine
from sqlalchemy.orm import declarative_base

USER = os.getenv("POSTGRES_USER", "playpup")
PASSWORD = os.getenv("POSTGRES_PASSWORD", "playpup")
DB_NAME = os.getenv("POSTGRES_DB", "playpup")
DB_HOST = os.getenv("DB_HOST", "postgres")

SQLALCHEMY_DATABASE_URL = f"postgresql+asyncpg://{USER}:{PASSWORD}@{DB_HOST}/{DB_NAME}"

engine = create_async_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = async_sessionmaker(engine, expire_on_commit=False)

Base = declarative_base()


async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with SessionLocal() as session:
        yield session
