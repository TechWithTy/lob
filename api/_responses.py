from __future__ import annotations

from typing import Generic, List, Optional, TypeVar

from pydantic import BaseModel, HttpUrl

T = TypeVar("T")


class ListResponse(BaseModel, Generic[T]):
    object: str = "list"
    data: List[T]
    next_url: Optional[HttpUrl] = None
    previous_url: Optional[HttpUrl] = None
    count: Optional[int] = None
    total_count: Optional[int] = None
