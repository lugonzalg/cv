from sqlalchemy import Column, Integer, String, Text
from pydantic import BaseModel
from ..data.database import Database

class AppProjectModel(Database.Base):
    __tablename__ = "app_project"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(Text)
    skills = Column(String)
    repo = Column(String)
