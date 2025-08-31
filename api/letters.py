from __future__ import annotations

from typing import Any, Dict, Optional

from ..client import LobClient
from ._requests import PaginationQuery, expand_metadata_filters
from ._responses import ListResponse
from ._models import Letter


async def list_letters(
    client: LobClient,
    *,
    pagination: Optional[PaginationQuery] = None,
    metadata: Optional[Dict[str, Any]] = None,
    extra_filters: Optional[Dict[str, Any]] = None,
) -> ListResponse[Letter]:
    params: Dict[str, Any] = {}
    if pagination:
        params.update(pagination.to_params())
    expand_metadata_filters(params, metadata)
    if extra_filters:
        params.update({k: v for k, v in extra_filters.items() if v is not None})
    
    return await client.request(
        "GET",
        "/letters",
        params=params,
        response_model=ListResponse[Letter],
    )


async def create_letter(
    client: LobClient,
    data: Dict[str, Any],
    *,
    idempotency_key: Optional[str] = None,
) -> Letter:
    return await client.request(
        "POST",
        "/letters",
        json=data,
        idempotency_key=idempotency_key,
        response_model=Letter,
    )


async def retrieve_letter(client: LobClient, letter_id: str) -> Letter:
    return await client.request(
        "GET",
        f"/letters/{letter_id}",
        response_model=Letter,
    )


async def cancel_letter(client: LobClient, letter_id: str) -> Dict[str, Any]:
    return await client.request("DELETE", f"/letters/{letter_id}")
