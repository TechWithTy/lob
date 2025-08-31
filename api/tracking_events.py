from __future__ import annotations

from typing import Any, Dict, Optional

from ..client import LobClient
from ._requests import PaginationQuery


async def list_tracking_events(
    client: LobClient,
    *,
    pagination: Optional[PaginationQuery] = None,
    filters: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    if pagination:
        params.update(pagination.to_params())
    if filters:
        params.update({k: v for k, v in filters.items() if v is not None})

    return await client.request("GET", "/tracking_events", params=params)
