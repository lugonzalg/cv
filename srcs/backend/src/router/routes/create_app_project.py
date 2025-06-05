from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from backend.data import get_session
from backend.services import AppRepoService
from backend.models import AppProject


class CreateAppProjectRoute:
    """Handle creating a project"""

    router = APIRouter()

    @staticmethod
    @router.post("/projects", response_model=AppProject)
    async def handle(app_project: AppProject, session: AsyncSession = Depends(get_session)):
        return await AppRepoService.create_project(session, app_project.model_dump())
