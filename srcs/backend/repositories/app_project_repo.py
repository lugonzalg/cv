from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from backend.models import Project

class AppProjectRepo:

    @staticmethod
    async def list_projects(self) -> list[AppProject]:
        result = await self.session.execute(select(Project))
        return result.scalars().all()
