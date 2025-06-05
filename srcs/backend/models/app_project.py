from sqlalchemy import Column, Integer, String, Text
from ..data.database import Base

class AppProject(Base):
    __tablename__ = "app_projects"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(Text)
    skills = Column(String)
    repo = Column(String)
