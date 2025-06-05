from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from ..data.database import get_session
from ..services.app_repo_service import AppRepoService
from ..models import ProjectUpdate, ProjectRead

router = APIRouter(prefix="/api")

class UpdateAppProject:
    """Handle updating a project"""

    @staticmethod
    @router.put("/projects/{project_id}", response_model=ProjectRead)
    async def handle(
        project_id: int,
        payload: ProjectUpdate,
        session: AsyncSession = Depends(get_session),
    ):
        project = await AppRepoService.update_project(
            session,
            project_id,
            {k: v for k, v in payload.dict().items() if v is not None},
        )
        if not project:
            raise HTTPException(status_code=404, detail="Project not found")
        return project
