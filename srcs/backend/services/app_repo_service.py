from ..repositories.app_repo import AppRepo

class AppRepoService:
    def __init__(self, repo: AppRepo):
        self.repo = repo

    async def get_projects(self):
        return await self.repo.list_projects()

