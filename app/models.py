from sqlmodel import Field, SQLModel
from typing import Optional
from datetime import datetime

class Link(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    code: str = Field(index=True, unique=True)
    target_url : str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    click_count: int = 0
    title: Optional[str] = None
