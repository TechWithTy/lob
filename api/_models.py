from __future__ import annotations

from datetime import datetime
from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field


class LobResource(BaseModel):
    id: str
    object: str
    created_at: Optional[datetime] = None
    deleted: Optional[bool] = None
    metadata: Optional[Dict[str, Any]] = None


# Print & Mail
class Postcard(LobResource):
    status: Optional[str] = None
    to: Optional[Dict[str, Any]] = None
    from_address: Optional[Dict[str, Any]] = Field(default=None, alias="from")
    front: Optional[Any] = None
    back: Optional[Any] = None


class Letter(LobResource):
    status: Optional[str] = None
    to: Optional[Dict[str, Any]] = None
    from_address: Optional[Dict[str, Any]] = Field(default=None, alias="from")
    file: Optional[Any] = None


class SelfMailer(LobResource):
    status: Optional[str] = None
    to: Optional[Dict[str, Any]] = None
    from_address: Optional[Dict[str, Any]] = Field(default=None, alias="from")
    inside: Optional[Any] = None
    outside: Optional[Any] = None


class Check(LobResource):
    status: Optional[str] = None
    amount: Optional[float] = None
    to: Optional[Dict[str, Any]] = None
    from_address: Optional[Dict[str, Any]] = Field(default=None, alias="from")


class SnapPack(LobResource):
    status: Optional[str] = None


class Booklet(LobResource):
    status: Optional[str] = None


# Templates
class Template(LobResource):
    name: Optional[str] = None
    description: Optional[str] = None
    published_version: Optional[str] = None


class TemplateVersion(LobResource):
    HTML: Optional[str] = None
    engine: Optional[str] = None
    description: Optional[str] = None


# Campaigns/Creatives/Uploads
class Campaign(LobResource):
    name: Optional[str] = None
    status: Optional[str] = None


class Creative(LobResource):
    name: Optional[str] = None
    resource_type: Optional[str] = None


class Upload(LobResource):
    filename: Optional[str] = None
    mimetype: Optional[str] = None
    size_bytes: Optional[int] = None


# Webhooks/Events
class Webhook(LobResource):
    url: Optional[str] = None
    enabled: Optional[bool] = None
    events: Optional[List[str]] = None


class Event(LobResource):
    type: Optional[str] = None
    body: Optional[Dict[str, Any]] = None


class TrackingEvent(LobResource):
    type: Optional[str] = None
    details: Optional[Dict[str, Any]] = None


# Special Features
class BillingGroup(LobResource):
    name: Optional[str] = None


class Buckslip(LobResource):
    description: Optional[str] = None


class BuckslipOrder(LobResource):
    buckslip_id: Optional[str] = None
    quantity: Optional[int] = None


class Card(LobResource):
    description: Optional[str] = None


class CardOrder(LobResource):
    card_id: Optional[str] = None
    quantity: Optional[int] = None


class QrCode(LobResource):
    qr_id: Optional[str] = Field(default=None, alias="qr_id")
    image_url: Optional[str] = None


class ShortUrl(LobResource):
    short_code: Optional[str] = None
    destination_url: Optional[str] = None


class BankAccount(LobResource):
    bank_name: Optional[str] = None
    last4: Optional[str] = None


# Verifications
class IntlVerificationResult(BaseModel):
    id: Optional[str] = None
    recipient: Optional[str] = None
    primary_line: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    postal_code: Optional[str] = None
    country: Optional[str] = None
    deliverability: Optional[str] = None
    components: Optional[Dict[str, Any]] = None


class IdentityValidationResult(BaseModel):
    id: Optional[str] = None
    confidence: Optional[float] = None
    matches: Optional[Dict[str, Any]] = None


class ReverseGeocodeResult(BaseModel):
    latitude: float
    longitude: float
    addresses: List[Dict[str, Any]]


class USZipLookupResult(BaseModel):
    zip_code: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    counties: Optional[List[Dict[str, Any]]] = None


__all__ = [
    # base
    "LobResource",
    # print & mail
    "Postcard",
    "Letter",
    "SelfMailer",
    "Check",
    "SnapPack",
    "Booklet",
    # templates
    "Template",
    "TemplateVersion",
    # campaigns/creatives/uploads
    "Campaign",
    "Creative",
    "Upload",
    # webhooks/events
    "Webhook",
    "Event",
    "TrackingEvent",
    # special features
    "BillingGroup",
    "Buckslip",
    "BuckslipOrder",
    "Card",
    "CardOrder",
    "QrCode",
    "ShortUrl",
    "BankAccount",
    # verifications
    "IntlVerificationResult",
    "IdentityValidationResult",
    "ReverseGeocodeResult",
    "USZipLookupResult",
]
