from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from ..data.database import get_session
from ..services.app_repo_service import AppRepoService
from ..models import ProjectRead

router = APIRouter(prefix="/api")

class GetAppProject:
    """Handle retrieving a single project"""

    @staticmethod
    @router.get("/projects/{project_id}", response_model=ProjectRead)
    async def handle(project_id: int, session: AsyncSession = Depends(get_session)):
        project = await AppRepoService.get_project(session, project_id)
        if not project:
            raise HTTPException(status_code=404, detail="Project not found")
        return project
