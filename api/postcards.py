from __future__ import annotations

from typing import Any, Dict, Optional

from ..client import LobClient
from ._requests import PaginationQuery, expand_metadata_filters
from ._responses import ListResponse
from ._models import Postcard


async def list_postcards(
    client: LobClient,
    *,
    pagination: Optional[PaginationQuery] = None,
    metadata: Optional[Dict[str, Any]] = None,
    extra_filters: Optional[Dict[str, Any]] = None,
) -> ListResponse[Postcard]:
    params: Dict[str, Any] = {}
    if pagination:
        params.update(pagination.to_params())
    expand_metadata_filters(params, metadata)
    if extra_filters:
        params.update({k: v for k, v in extra_filters.items() if v is not None})
    
    return await client.request(
        "GET",
        "/postcards",
        params=params,
        response_model=ListResponse[Postcard],
    )


async def create_postcard(
    client: LobClient,
    data: Dict[str, Any],
    *,
    idempotency_key: Optional[str] = None,
) -> Postcard:
    return await client.request(
        "POST",
        "/postcards",
        json=data,
        idempotency_key=idempotency_key,
        response_model=Postcard,
    )


async def retrieve_postcard(client: LobClient, postcard_id: str) -> Postcard:
    return await client.request(
        "GET",
        f"/postcards/{postcard_id}",
        response_model=Postcard,
    )


async def cancel_postcard(client: LobClient, postcard_id: str) -> Dict[str, Any]:
    return await client.request("DELETE", f"/postcards/{postcard_id}")
