from pydantic import BaseModel, HttpUrl
from typing import Optional

class ShortenRequest(BaseModel):
    url: HttpUrl
    custom_code: Optional[str] = None
    title: Optional[str] = None

class ShortenResponse(BaseModel):
    code: str
    short_url: HttpUrl
    target_url: HttpUrl


class StatsResponse(BaseModel):
    code: str
    target_url: HttpUrl
    click_count: int
    created_at: str
    title: Optional[str] = None