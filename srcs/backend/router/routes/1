from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from backend.data import get_session
from backend.services import AppRepoService


class DeleteAppProjectRoute:
    """Handle deleting a project"""

    router = APIRouter()

    @staticmethod
    @router.delete("/projects/{project_id}")
    async def handle(project_id: int, session: AsyncSession = Depends(get_session)):
        success = await AppRepoService.delete_project(session, project_id)
        if not success:
            raise HTTPException(status_code=404, detail="Project not found")
        return {"deleted": project_id}
