from fastapi import APIRouter, Depends
from ..data.database import get_session
from ..repositories.app_repo import AppRepo
from ..services.app_repo_service import AppRepoService

router = APIRouter(prefix="/api")

async def get_service(session=Depends(get_session)):
    repo = AppRepo(session)
    return AppRepoService(repo)

@router.get("/projects")
async def list_projects(service: AppRepoService = Depends(get_service)):
    return await service.get_projects()
