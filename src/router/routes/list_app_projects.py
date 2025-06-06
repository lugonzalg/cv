from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.data import Database
from src.repositories import AppProjectRepo
from src.models import AppProjectDTO


class ListAppProjectsRoute:
    """Handle listing projects"""

    router = APIRouter()

    @staticmethod
    @router.get("/projects", response_model=list[AppProjectDTO])
    async def handle(session: AsyncSession = Depends(Database.get_session)):
        return await AppProjectRepo.list_projects(session)
