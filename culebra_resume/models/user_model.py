from pydantic import BaseModel
from sqlmodel import Field, Session, SQLModel


class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    position: str = Field()
    