from __future__ import annotations

from typing import Any, Dict, Optional

from ..client import LobClient


async def us_zip_lookup(
    client: LobClient,
    *,
    zip_code: Optional[str] = None,
    city: Optional[str] = None,
    state: Optional[str] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    if zip_code is not None:
        params["zip_code"] = zip_code
    if city is not None:
        params["city"] = city
    if state is not None:
        params["state"] = state

    return await client.request("GET", "/us_zip_lookups", params=params)
