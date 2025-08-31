from __future__ import annotations

from typing import Any, Dict, Optional

from ..client import LobClient
from ._requests import PaginationQuery
from ._responses import ListResponse
from ._models import Webhook


async def list_webhooks(
    client: LobClient,
    *,
    pagination: Optional[PaginationQuery] = None,
) -> ListResponse[Webhook]:
    params = pagination.to_params() if pagination else {}
    return await client.request(
        "GET",
        "/webhooks",
        params=params,
        response_model=ListResponse[Webhook],
    )


async def create_webhook(
    client: LobClient,
    data: Dict[str, Any],
) -> Webhook:
    return await client.request(
        "POST",
        "/webhooks",
        json=data,
        response_model=Webhook,
    )


async def retrieve_webhook(client: LobClient, webhook_id: str) -> Webhook:
    return await client.request(
        "GET",
        f"/webhooks/{webhook_id}",
        response_model=Webhook,
    )


async def delete_webhook(client: LobClient, webhook_id: str) -> Dict[str, Any]:
    return await client.request("DELETE", f"/webhooks/{webhook_id}")
