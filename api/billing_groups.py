from __future__ import annotations

from typing import Any, Dict, Optional

from ..client import LobClient
from ._requests import PaginationQuery


async def list_billing_groups(
    client: LobClient,
    *,
    pagination: Optional[PaginationQuery] = None,
) -> Dict[str, Any]:
    params = pagination.to_params() if pagination else {}
    return await client.request("GET", "/billing_groups", params=params)


async def create_billing_group(
    client: LobClient,
    data: Dict[str, Any],
) -> Dict[str, Any]:
    return await client.request("POST", "/billing_groups", json=data)


async def retrieve_billing_group(client: LobClient, group_id: str) -> Dict[str, Any]:
    return await client.request("GET", f"/billing_groups/{group_id}")


async def delete_billing_group(client: LobClient, group_id: str) -> Dict[str, Any]:
    return await client.request("DELETE", f"/billing_groups/{group_id}")
