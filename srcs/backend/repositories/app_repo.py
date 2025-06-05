from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from ..models import Project


class AppRepo:
    """Repository with static CRUD operations for :class:`Project`."""

    @staticmethod
    async def list_projects(session: AsyncSession):
        result = await session.execute(select(Project))
        return result.scalars().all()

    @staticmethod
    async def create_project(session: AsyncSession, project: Project) -> Project:
        session.add(project)
        await session.commit()
        await session.refresh(project)
        return project

    @staticmethod
    async def get_project(session: AsyncSession, project_id: int) -> Project | None:
        return await session.get(Project, project_id)

    @staticmethod
    async def update_project(session: AsyncSession, project_id: int, data: dict) -> Project | None:
        project = await session.get(Project, project_id)
        if not project:
            return None
        for key, value in data.items():
            setattr(project, key, value)
        await session.commit()
        await session.refresh(project)
        return project

    @staticmethod
    async def delete_project(session: AsyncSession, project_id: int) -> bool:
        project = await session.get(Project, project_id)
        if not project:
            return False
        await session.delete(project)
        await session.commit()
        return True
