from __future__ import annotations

from typing import Any, Dict

from ..client import LobClient


async def reverse_geocode(
    client: LobClient,
    *,
    latitude: float,
    longitude: float,
) -> Dict[str, Any]:
    params = {"latitude": latitude, "longitude": longitude}
    return await client.request("GET", "/reverse_geocode", params=params)
