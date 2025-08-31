from __future__ import annotations

from typing import Any, Dict, Optional

from ..client import LobClient
from ._requests import PaginationQuery, expand_metadata_filters
from ._responses import ListResponse
from ._models import SelfMailer


async def list_self_mailers(
    client: LobClient,
    *,
    pagination: Optional[PaginationQuery] = None,
    metadata: Optional[Dict[str, Any]] = None,
    extra_filters: Optional[Dict[str, Any]] = None,
) -> ListResponse[SelfMailer]:
    params: Dict[str, Any] = {}
    if pagination:
        params.update(pagination.to_params())
    expand_metadata_filters(params, metadata)
    if extra_filters:
        params.update({k: v for k, v in extra_filters.items() if v is not None})
    
    return await client.request(
        "GET",
        "/self_mailers",
        params=params,
        response_model=ListResponse[SelfMailer],
    )


async def create_self_mailer(
    client: LobClient,
    data: Dict[str, Any],
    *,
    idempotency_key: Optional[str] = None,
) -> SelfMailer:
    return await client.request(
        "POST",
        "/self_mailers",
        json=data,
        idempotency_key=idempotency_key,
        response_model=SelfMailer,
    )


async def retrieve_self_mailer(client: LobClient, sm_id: str) -> SelfMailer:
    return await client.request(
        "GET",
        f"/self_mailers/{sm_id}",
        response_model=SelfMailer,
    )


async def cancel_self_mailer(client: LobClient, sm_id: str) -> Dict[str, Any]:
    return await client.request("DELETE", f"/self_mailers/{sm_id}")
