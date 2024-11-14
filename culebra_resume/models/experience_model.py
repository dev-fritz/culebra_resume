from datetime import date
from sqlmodel import SQLModel, Field


class Experience(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    start_date: date = Field()
    end_date: date | None = Field(default=None, nullable=True)
    user_id: int = Field(foreign_key="user.id")

    position_title: str = Field(max_length=100)
    company_name: str = Field(max_length=100)
    location: str | None = Field(default="Remote", max_length=100)
    description: str | None = Field(default=None, nullable= True)
    employment_type: str | None = Field(default=None, max_length=50, nullable=True)
