from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from ..data.database import get_session
from ..services.app_repo_service import AppRepoService

router = APIRouter(prefix="/api")

class DeleteAppProject:
    """Handle deleting a project"""

    @staticmethod
    @router.delete("/projects/{project_id}")
    async def handle(project_id: int, session: AsyncSession = Depends(get_session)):
        success = await AppRepoService.delete_project(session, project_id)
        if not success:
            raise HTTPException(status_code=404, detail="Project not found")
        return {"deleted": project_id}
