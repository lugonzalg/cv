from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.data import Database
from src.repositories import AppProjectRepo
from src.models import AppProjectModel


class CreateAppProjectRoute:
    """Handle creating a project"""

    router = APIRouter()

    @staticmethod
    @router.post("/projects", response_model=AppProjectModel)
    async def handle(
        app_project: AppProjectModel,
        session: AsyncSession = Depends(Database.get_session),
    ):
        return await AppProjectRepo.create_project(session, app_project.model_dump())
