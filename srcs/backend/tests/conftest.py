import pytest
import pytest_asyncio

from src.data import Database
from src.settings import AppSettings
from src.repositories import AppProjectRepo
import os
from unittest.mock import AsyncMock, MagicMock

@pytest_asyncio.fixture(scope="session", autouse=True)
async def setup_database():
    settings = AppSettings()

    await Database.initialize(
        settings.DB_URL,
    )

@pytest.fixture(scope="session")
def mock_session():
    mock_session = AsyncMock()
    mock_session.add = MagicMock()
    yield mock_session

@pytest_asyncio.fixture(scope="session")
async def session():
    """Fixture to create a database session for testing."""
    async with Database.session() as session:
        yield session

def create_random_app_project():
    return AppProjectRepo.model_factory(
        name=os.urandom(8).hex(),
        description=os.urandom(16).hex(),
        skills=os.urandom(8).hex(),
        repo=os.urandom(4).hex(),
    )

def create_random_app_project_list(count=5):
    return [create_random_app_project() for _ in range(count)]