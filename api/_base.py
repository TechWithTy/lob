from __future__ import annotations

from datetime import datetime
from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field, HttpUrl


class Address(BaseModel):
    id: str
    object: str = "address"
    name: Optional[str] = None
    company: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    address_line1: Optional[str] = None
    address_line2: Optional[str] = None
    address_city: Optional[str] = None
    address_state: Optional[str] = None
    address_zip: Optional[str] = None
    address_country: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    date_created: Optional[datetime] = None
    date_modified: Optional[datetime] = None


class AddressCreate(BaseModel):
    name: Optional[str] = None
    company: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    address_line1: str
    address_line2: Optional[str] = None
    address_city: str
    address_state: Optional[str] = None
    address_zip: Optional[str] = None
    address_country: str = "US"
    metadata: Optional[Dict[str, Any]] = None


class AddressListResponse(BaseModel):
    object: str = "list"
    data: List[Address] = Field(default_factory=list)
    next_url: Optional[HttpUrl] = None
    previous_url: Optional[HttpUrl] = None
    count: Optional[int] = None


class DeleteResponse(BaseModel):
    id: str
    deleted: bool