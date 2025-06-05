from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from backend.data import get_session
from backend.services import AppRepoService
from backend.models import AppProject


class GetAppProjectRoute:
    """Handle retrieving a single project"""

    router = APIRouter()

    @staticmethod
    @router.get("/projects/{project_id}", response_model=AppProject)
    async def handle(project_id: int, session: AsyncSession = Depends(get_session)):
        project = await AppRepoService.get_project(session, project_id)
        if not project:
            raise HTTPException(status_code=404, detail="Project not found")
        return project
