import pytest_asyncio

from src.data import Database
from src.settings import AppSettings
from src.models import AppProjectModel
from src.repositories import AppProjectRepo
import os

@pytest_asyncio.fixture(scope="session", autouse=True)
async def setup_database():
    settings = AppSettings()

    await Database.initialize(
        settings.DB_URL,
    )


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