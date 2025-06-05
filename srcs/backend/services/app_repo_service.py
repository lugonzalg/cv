from ..repositories.app_repo import AppRepo
from sqlalchemy.ext.asyncio import AsyncSession
from ..models import Project


class AppRepoService:
    """Service layer delegating to :class:`AppRepo`. All methods are static."""

    @staticmethod
    async def get_projects(session: AsyncSession):
        return await AppRepo.list_projects(session)

    @staticmethod
    async def create_project(session: AsyncSession, project: Project) -> Project:
        return await AppRepo.create_project(session, project)

    @staticmethod
    async def get_project(session: AsyncSession, project_id: int) -> Project | None:
        return await AppRepo.get_project(session, project_id)

    @staticmethod
    async def update_project(session: AsyncSession, project_id: int, data: dict) -> Project | None:
        return await AppRepo.update_project(session, project_id, data)

    @staticmethod
    async def delete_project(session: AsyncSession, project_id: int) -> bool:
        return await AppRepo.delete_project(session, project_id)

