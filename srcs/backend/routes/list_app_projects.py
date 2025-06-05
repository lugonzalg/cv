from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from ..data.database import get_session
from ..services.app_repo_service import AppRepoService
from ..models import ProjectRead

router = APIRouter(prefix="/api")

class ListAppProjects:
    """Handle listing projects"""

    @staticmethod
    @router.get("/projects", response_model=list[ProjectRead])
    async def handle(session: AsyncSession = Depends(get_session)):
        return await AppRepoService.get_projects(session)
