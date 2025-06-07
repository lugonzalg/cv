from fastapi import APIRouter
from src.models import AppProjectDTO
from src.controllers import CreateAppProjectController
from sqlalchemy.ext.asyncio import AsyncSession
from src.data import Database
from fastapi import Depends


class CreateAppProjectRoute:
    """Handle creating a project"""

    router = APIRouter()

    @staticmethod
    @router.post("/project", response_model=AppProjectDTO)
    async def handler(
        app_project: AppProjectDTO,
        session: AsyncSession = Depends(Database.get_session),
    ):
        result = await CreateAppProjectController.handler(session, app_project)
        return result
