import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

USER = os.getenv("POSTGRES_USER", "playpup")
PASSWORD = os.getenv("POSTGRES_PASSWORD", "playpup")
DB_NAME = os.getenv("POSTGRES_DB", "playpup")
DB_HOST = os.getenv("DB_HOST", "postgres")

SQLALCHEMY_DATABASE_URL = f"postgresql://{USER}:{PASSWORD}@{DB_HOST}/{DB_NAME}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_session():
    with SessionLocal() as session:
        yield session
