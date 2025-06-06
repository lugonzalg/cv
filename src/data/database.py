from contextlib import asynccontextmanager
from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker,
    AsyncSession,
    AsyncEngine,
)
from sqlalchemy.orm import declarative_base

from typing import Optional, Any
from pydantic_core import MultiHostUrl
from sqlmodel import SQLModel


class Database:
    """Database helper exposing an async session context manager."""

    engine: Optional[AsyncEngine] = None
    base: Optional[Any] = None

    @classmethod
    async def initialize(cls, url: MultiHostUrl) -> None:
        """Initialize the database with the provided URL."""

        if not url:
            raise ValueError("Invalid database URL provided.")

        if not isinstance(url, MultiHostUrl):
            raise TypeError("Database URL must be of type MultiHostUrl.")

        cls.engine = create_async_engine(url, echo=False)
        cls.engine = create_async_engine(url, echo=False)
        cls.SessionLocal = async_sessionmaker(cls.engine, expire_on_commit=False)
        cls.Base = declarative_base()

        SQLModel.metadata.create_all(cls.engine)

    @classmethod
    @asynccontextmanager
    async def session(cls) -> AsyncSession:
        async with cls.SessionLocal() as session:
            yield session

    @classmethod
    async def get_session(cls) -> AsyncSession:
        async with cls.session() as session:
            yield session
