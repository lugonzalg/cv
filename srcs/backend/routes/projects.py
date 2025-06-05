from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from ..data.database import get_session
from ..services.app_repo_service import AppRepoService
from ..models import ProjectCreate, ProjectUpdate, ProjectRead, Project

router = APIRouter(prefix="/api")

@router.get("/projects", response_model=list[ProjectRead])
async def list_app_projects(session: AsyncSession = Depends(get_session)):
    return await AppRepoService.get_projects(session)


@router.post("/projects", response_model=ProjectRead)
async def create_app_project(
    payload: ProjectCreate, session: AsyncSession = Depends(get_session)
):
    project = Project(**payload.dict())
    return await AppRepoService.create_project(session, project)


@router.get("/projects/{project_id}", response_model=ProjectRead)
async def get_app_project(project_id: int, session: AsyncSession = Depends(get_session)):
    project = await AppRepoService.get_project(session, project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    return project


@router.put("/projects/{project_id}", response_model=ProjectRead)
async def update_app_project(
    project_id: int,
    payload: ProjectUpdate,
    session: AsyncSession = Depends(get_session),
):
    project = await AppRepoService.update_project(
        session, project_id, {k: v for k, v in payload.dict().items() if v is not None}
    )
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    return project


@router.delete("/projects/{project_id}")
async def delete_app_project(project_id: int, session: AsyncSession = Depends(get_session)):
    success = await AppRepoService.delete_project(session, project_id)
    if not success:
        raise HTTPException(status_code=404, detail="Project not found")
    return {"deleted": project_id}
