from __future__ import annotations

from typing import Any, Dict, Optional

from ..client import LobClient
from ._requests import PaginationQuery


async def list_booklets(
    client: LobClient,
    *,
    pagination: Optional[PaginationQuery] = None,
) -> Dict[str, Any]:
    params = pagination.to_params() if pagination else {}
    return await client.request("GET", "/booklets", params=params)


async def create_booklet(
    client: LobClient,
    data: Dict[str, Any],
    *,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    return await client.request(
        "POST", "/booklets", json=data, idempotency_key=idempotency_key
    )


async def retrieve_booklet(client: LobClient, booklet_id: str) -> Dict[str, Any]:
    return await client.request("GET", f"/booklets/{booklet_id}")


async def cancel_booklet(client: LobClient, booklet_id: str) -> Dict[str, Any]:
    return await client.request("DELETE", f"/booklets/{booklet_id}")
