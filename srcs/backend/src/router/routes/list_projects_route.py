from fastapi import APIRouter, Depends
from backend.data.database import get_session
from backend.repositories import AppProjectRepo

class ListProjectsRoute:

    router = APIRouter()

    @staticmethod
    @router.get("/projects")
    async def list_projects():
        pass
