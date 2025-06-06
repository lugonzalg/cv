from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.data import Database
from src.router import app_router
from src.settings import AppSettings


async def lifespan(app: FastAPI):
    app.state.settings = AppSettings()

    await Database.initialize(
        app.state.settings.DB_URL,
    )

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
