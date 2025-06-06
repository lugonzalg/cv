from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.data import Database
from src.repositories import AppProjectRepo
from src.models import AppProjectModel


class ListAppProjectsRoute:
    """Handle listing projects"""

    router = APIRouter()

    @staticmethod
    @router.get("/projects", response_model=list[AppProjectModel])
    async def handle(session: AsyncSession = Depends(Database.get_session)):
        return await AppProjectRepo.get_project(session)
