from datetime import date
from sqlmodel import SQLModel, Field


class Education(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    start_date: date = Field()
    end_date: date | None = Field(default=None, nullable=True)
    user_id: int = Field(foreign_key="user.id")

    institution_name: str = Field(max_length=100)
    degree: str | None = Field(default=None, max_length=50, nullable=True)
    field_of_study: str | None = Field(default=None, max_length=100, nullable=True)
    description: str | None = Field(default=None, nullable=True)
    status: str | None = Field(default="in_progress", max_length=20)
