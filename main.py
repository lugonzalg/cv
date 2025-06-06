from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.data import Database

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
