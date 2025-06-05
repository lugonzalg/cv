from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from backend.models import AppProject

class AppProjectRepo:

    @staticmethod
    async def list_projects(self) -> list[AppProject]:
        result = await self.session.execute(select(AppProject))
        return result.scalars().all()
