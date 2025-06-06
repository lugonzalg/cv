from sqlmodel import SQLModel, Field


class AppProjectModel(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str
    description: str
    skills: str
    repo: str
