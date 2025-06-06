from .base import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String

from pydantic import BaseModel


class AppProjectModel(Base):
    __tablename__ = "app_project"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(30), unique=True)
    description: Mapped[str] = mapped_column(nullable=False)
    skills: Mapped[str] = mapped_column(nullable=False)
    repo: Mapped[str] = mapped_column(nullable=False, unique=True)

    def __repr__(self) -> str:
        return f"AppProjectModel(name={self.name}, skills={self.skills})"


class AppProjectDTO(BaseModel):
    name: str
    description: str
    skills: str
    repo: str

    def __repr__(self) -> str:
        return f"AppProjectDTO(name={self.name}, skills={self.skills})"
