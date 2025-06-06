from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from src.data import Database
from src.repositories import AppProjectRepo
from src.models import AppProjectDTO


class GetAppProjectRoute:
    """Handle retrieving a single project"""

    router = APIRouter()

    @staticmethod
    @router.get("/projects/{project_id}", response_model=AppProjectDTO)
    async def handle(
        project_id: int, session: AsyncSession = Depends(Database.get_session)
    ):
        project = await AppProjectRepo.get_project(session, project_id)
        if not project:
            raise HTTPException(status_code=404, detail="Project not found")
        return project
