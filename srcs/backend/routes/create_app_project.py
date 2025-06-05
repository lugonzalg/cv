from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from ..data.database import get_session
from ..services.app_repo_service import AppRepoService
from ..models import ProjectCreate, ProjectRead, Project

router = APIRouter(prefix="/api")

class CreateAppProject:
    """Handle creating a project"""

    @staticmethod
    @router.post("/projects", response_model=ProjectRead)
    async def handle(payload: ProjectCreate, session: AsyncSession = Depends(get_session)):
        project = Project(**payload.dict())
        return await AppRepoService.create_project(session, project)
