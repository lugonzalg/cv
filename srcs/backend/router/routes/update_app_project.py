from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from backend.data import get_session
from backend.services import AppRepoService
from backend.models import AppProject


class UpdateAppProject:
    """Handle updating a project"""
    router = APIRouter()

    @staticmethod
    @router.put("/projects/{project_id}", response_model=AppProject)
    async def handle(
        project_id: int,
        app_project: AppProject,
        session: AsyncSession = Depends(get_session),
    ):
        project = await AppRepoService.update_project(
            session,
            project_id,
            {k: v for k, v in app_project.model_dump().items() if v is not None},
        )
        if not project:
            raise HTTPException(status_code=404, detail="Project not found")
        return project
