from __future__ import annotations

from typing import Any, Dict, Optional

from ..client import LobClient
from ._requests import PaginationQuery


async def list_snap_packs(
    client: LobClient,
    *,
    pagination: Optional[PaginationQuery] = None,
) -> Dict[str, Any]:
    params = pagination.to_params() if pagination else {}
    return await client.request("GET", "/snap_packs", params=params)


async def create_snap_pack(
    client: LobClient,
    data: Dict[str, Any],
    *,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    return await client.request(
        "POST", "/snap_packs", json=data, idempotency_key=idempotency_key
    )


async def retrieve_snap_pack(client: LobClient, snap_pack_id: str) -> Dict[str, Any]:
    return await client.request("GET", f"/snap_packs/{snap_pack_id}")


async def cancel_snap_pack(client: LobClient, snap_pack_id: str) -> Dict[str, Any]:
    return await client.request("DELETE", f"/snap_packs/{snap_pack_id}")
