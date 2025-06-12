from contextlib import asynccontextmanager
from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker,
    AsyncSession,
    AsyncEngine,
)

from typing import Optional, Any, AsyncGenerator
from pydantic_core import MultiHostUrl
from src.models import Base


class Database:
    """Database helper exposing an async session context manager."""

    engine: Optional[AsyncEngine] = None
    base: Optional[Any] = None

    @classmethod
    async def initialize(
        cls,
        url: MultiHostUrl,
    ) -> None:
        """Initialize the database with the provided URL."""

        if not url:
            raise ValueError("Invalid database URL provided.")

        if not isinstance(url, MultiHostUrl):
            raise TypeError("Database URL must be of type MultiHostUrl.")

        cls.engine = create_async_engine(str(url), echo=False)
        cls.SessionLocal = async_sessionmaker(cls.engine, expire_on_commit=False)

        async with cls.engine.begin() as conn:
            # Create all tables in the database
            await conn.run_sync(Base.metadata.create_all)

    @classmethod
    @asynccontextmanager
    async def session(cls) -> AsyncGenerator[... ,AsyncSession]:
        async with cls.SessionLocal() as session:
            yield session