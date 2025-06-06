import os
from contextlib import asynccontextmanager
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import declarative_base


class Database:
    """Database helper exposing an async session context manager."""

    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite+aiosqlite:///./test.db")
    engine = create_async_engine(DATABASE_URL, echo=False)
    SessionLocal = async_sessionmaker(engine, expire_on_commit=False)
    Base = declarative_base()

    @staticmethod
    @asynccontextmanager
    async def session() -> AsyncSession:
        async with Database.SessionLocal() as session:
            yield session

    @staticmethod
    async def get_session() -> AsyncSession:
        async with Database.session() as session:
            yield session


Base = Database.Base
