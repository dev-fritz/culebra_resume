from datetime import datetime
from sqlmodel import SQLModel, Field

class Transaction(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    amount: int = Field(default=0, index=True)
    created: datetime = Field(default=datetime.now(), index=True, nullable=False)
    updated: datetime | None = Field(default=None, nullable=True)
    user_id: int = Field(foreign_key="user.id")

    description: str | None = Field(default=None, max_length=255)
    status: str = Field(default="pending", max_length=20)
    payment_method: str | None = Field(default="PIX", max_length=20)
    external_id: str | None = Field(default=None, max_length=100)
    currency: str = Field(default="BRL", max_length=3)
    fee: int | None = Field(default=0)
