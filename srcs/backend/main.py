from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routes import (
    list_app_projects_router,
    create_app_project_router,
    get_app_project_router,
    update_app_project_router,
    delete_app_project_router,
)
from .data.database import Database

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def on_startup():
    async with Database.engine.begin() as conn:
        await conn.run_sync(Database.Base.metadata.create_all)

app.include_router(list_app_projects_router)
app.include_router(create_app_project_router)
app.include_router(get_app_project_router)
app.include_router(update_app_project_router)
app.include_router(delete_app_project_router)
