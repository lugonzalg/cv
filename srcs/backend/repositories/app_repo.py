from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from ..models import Project

class AppRepo:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def list_projects(self):
        result = await self.session.execute(select(Project))
        return result.scalars().all()
