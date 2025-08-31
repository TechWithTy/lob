from __future__ import annotations

from typing import Any, Dict, Optional

from ..client import LobClient
from ._requests import PaginationQuery


async def list_card_orders(
    client: LobClient,
    *,
    pagination: Optional[PaginationQuery] = None,
) -> Dict[str, Any]:
    params = pagination.to_params() if pagination else {}
    return await client.request("GET", "/card_orders", params=params)


async def create_card_order(
    client: LobClient,
    data: Dict[str, Any],
) -> Dict[str, Any]:
    return await client.request("POST", "/card_orders", json=data)


async def retrieve_card_order(client: LobClient, order_id: str) -> Dict[str, Any]:
    return await client.request("GET", f"/card_orders/{order_id}")
