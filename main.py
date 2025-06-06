from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.data import Database
from src.router import app_router


async def lifespan(app: FastAPI):
    async with Database.engine.begin() as conn:
        await conn.run_sync(Database.Base.metadata.create_all)

    yield


app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(app_router.router)
