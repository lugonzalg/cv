from sqlalchemy import Column, Integer, String, Text
from pydantic import BaseModel
from ..data.database import Database

class Project(Database.Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(Text)
    skills = Column(String)
    repo = Column(String)


class ProjectBase(BaseModel):
    name: str
    description: str | None = None
    skills: str | None = None
    repo: str | None = None


class ProjectCreate(ProjectBase):
    pass


class ProjectUpdate(BaseModel):
    name: str | None = None
    description: str | None = None
    skills: str | None = None
    repo: str | None = None


class ProjectRead(ProjectBase):
    id: int

    class Config:
        orm_mode = True
