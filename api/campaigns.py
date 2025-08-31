from __future__ import annotations

from typing import Any, Dict, Optional

from ..client import LobClient
from ._requests import PaginationQuery


async def list_campaigns(
    client: LobClient,
    *,
    pagination: Optional[PaginationQuery] = None,
) -> Dict[str, Any]:
    params = pagination.to_params() if pagination else {}
    return await client.request("GET", "/campaigns", params=params)


async def create_campaign(
    client: LobClient,
    data: Dict[str, Any],
    *,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    return await client.request(
        "POST", "/campaigns", json=data, idempotency_key=idempotency_key
    )


async def retrieve_campaign(client: LobClient, campaign_id: str) -> Dict[str, Any]:
    return await client.request("GET", f"/campaigns/{campaign_id}")


async def delete_campaign(client: LobClient, campaign_id: str) -> Dict[str, Any]:
    return await client.request("DELETE", f"/campaigns/{campaign_id}")
