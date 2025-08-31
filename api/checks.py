from __future__ import annotations

from typing import Any, Dict, Optional

from ..client import LobClient
from ._requests import PaginationQuery, expand_metadata_filters


async def list_checks(
    client: LobClient,
    *,
    pagination: Optional[PaginationQuery] = None,
    metadata: Optional[Dict[str, Any]] = None,
    extra_filters: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    if pagination:
        params.update(pagination.to_params())
    expand_metadata_filters(params, metadata)
    if extra_filters:
        params.update({k: v for k, v in extra_filters.items() if v is not None})

    return await client.request("GET", "/checks", params=params)


async def create_check(
    client: LobClient,
    data: Dict[str, Any],
    *,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    return await client.request(
        "POST",
        "/checks",
        json=data,
        idempotency_key=idempotency_key,
    )


async def retrieve_check(client: LobClient, check_id: str) -> Dict[str, Any]:
    return await client.request("GET", f"/checks/{check_id}")


async def cancel_check(client: LobClient, check_id: str) -> Dict[str, Any]:
    return await client.request("DELETE", f"/checks/{check_id}")
