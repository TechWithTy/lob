from __future__ import annotations

from typing import Any, Dict, Optional

from ..client import LobClient
from ._requests import PaginationQuery


async def list_cards(
    client: LobClient,
    *,
    pagination: Optional[PaginationQuery] = None,
) -> Dict[str, Any]:
    params = pagination.to_params() if pagination else {}
    return await client.request("GET", "/cards", params=params)


async def create_card(
    client: LobClient,
    data: Dict[str, Any],
    *,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    return await client.request(
        "POST", "/cards", json=data, idempotency_key=idempotency_key
    )


async def retrieve_card(client: LobClient, card_id: str) -> Dict[str, Any]:
    return await client.request("GET", f"/cards/{card_id}")


async def delete_card(client: LobClient, card_id: str) -> Dict[str, Any]:
    return await client.request("DELETE", f"/cards/{card_id}")
