from __future__ import annotations

from typing import Any, Dict, Optional

from ..client import LobClient


async def verify_us_address(
    client: LobClient,
    *,
    primary_line: Optional[str] = None,
    secondary_line: Optional[str] = None,
    city: Optional[str] = None,
    state: Optional[str] = None,
    zip_code: Optional[str] = None,
    address_line1: Optional[str] = None,
    address_line2: Optional[str] = None,
) -> Dict[str, Any]:
    """US Verification (single).

    Docs: https://docs.lob.com/#tag/Address-Verification-API/operation/us_verifications
    Accepts either (primary_line/secondary_line) or (address_line1/address_line2).
    Returns the raw verification response as a dict for now.
    """
    payload: Dict[str, Any] = {}
    if primary_line is not None:
        payload["primary_line"] = primary_line
    if secondary_line is not None:
        payload["secondary_line"] = secondary_line
    if city is not None:
        payload["city"] = city
    if state is not None:
        payload["state"] = state
    if zip_code is not None:
        payload["zip_code"] = zip_code
    if address_line1 is not None:
        payload["address_line1"] = address_line1
    if address_line2 is not None:
        payload["address_line2"] = address_line2

    return await client.request("POST", "/us_verifications", json=payload)


async def verify_us_bulk(
    client: LobClient,
    addresses: list[Dict[str, Any]],
) -> Dict[str, Any]:
    """US Verification (bulk). Up to Lob's allowed batch size.

    Docs: https://docs.lob.com/#tag/Address-Verification-API/operation/us_verifications_bulk
    """
    payload = {"addresses": addresses}
    return await client.request("POST", "/us_verifications/bulk", json=payload)
