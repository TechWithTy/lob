from __future__ import annotations

from typing import Any, Dict, Optional

from ..client import LobClient


async def autocomplete_us_address(
    client: LobClient,
    *,
    address_prefix: str,
    city: Optional[str] = None,
    state: Optional[str] = None,
    zip_code: Optional[str] = None,
    country: str = "US",
    geo_ip_sort: Optional[bool] = None,
    size: Optional[int] = None,
) -> Dict[str, Any]:
    """US Autocompletions.

    Docs: https://docs.lob.com/#tag/Address-Verification-API/operation/us_autocompletions
    Returns raw dict for now.
    """
    payload: Dict[str, Any] = {
        "address_prefix": address_prefix,
        "country": country,
    }
    if city is not None:
        payload["city"] = city
    if state is not None:
        payload["state"] = state
    if zip_code is not None:
        payload["zip_code"] = zip_code
    if geo_ip_sort is not None:
        payload["geo_ip_sort"] = geo_ip_sort
    if size is not None:
        payload["size"] = size

    return await client.request("POST", "/us_autocompletions", json=payload)
