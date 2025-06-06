from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from backend.data import get_session
from backend.services import AppRepoService
from backend.models import AppProject


class ListAppProjects:
    """Handle listing projects"""

    router = APIRouter()

    @staticmethod
    @router.get("/projects", response_model=list[AppProject])
    async def handle(session: AsyncSession = Depends(get_session)):
        return await AppRepoService.get_projects(session)
