from datetime import date

from sqlmodel import SQLModel, Field


class Hability(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True, unique=True)
    description: str | None = Field(default=None, max_length=120, nullable=True)
    created_by: int | None = Field(default=None, foreign_key="user.id", nullable=True)
    created_in: date | None = Field(default=None, nullable=True)
