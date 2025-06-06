from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from src.data import Database
from src.repositories import AppProjectRepo
from src.models import AppProjectDTO


class UpdateAppProjectRoute:
    """Handle updating a project"""

    router = APIRouter()

    @staticmethod
    @router.put("/projects/{project_id}", response_model=AppProjectDTO)
    async def handle(
        project_id: int,
        app_project: AppProjectDTO,
        session: AsyncSession = Depends(Database.get_session),
    ):
        project = await AppProjectRepo.update_project(
            session,
            project_id,
            {k: v for k, v in app_project.model_dump().items() if v is not None},
        )
        if not project:
            raise HTTPException(status_code=404, detail="Project not found")
        return project
