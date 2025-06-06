from .routes import (
    CreateAppProjectRoute,
    ListAppProjectsRoute,
    GetAppProjectRoute,
    UpdateAppProjectRoute,
    DeleteAppProjectRoute,
)

from fastapi import APIRouter

router = APIRouter()

router.include_router(ListAppProjectsRoute.router)
router.include_router(CreateAppProjectRoute.router)
router.include_router(GetAppProjectRoute.router)
router.include_router(UpdateAppProjectRoute.router)
router.include_router(DeleteAppProjectRoute.router)
