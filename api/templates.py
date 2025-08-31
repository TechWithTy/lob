from __future__ import annotations

from typing import Any, Dict, Optional

from ..client import LobClient
from ._requests import PaginationQuery
from ._responses import ListResponse
from ._models import Template


async def list_templates(
    client: LobClient,
    *,
    pagination: Optional[PaginationQuery] = None,
) -> ListResponse[Template]:
    params = pagination.to_params() if pagination else {}
    return await client.request(
        "GET",
        "/templates",
        params=params,
        response_model=ListResponse[Template],
    )


async def create_template(
    client: LobClient,
    data: Dict[str, Any],
    *,
    idempotency_key: Optional[str] = None,
) -> Template:
    return await client.request(
        "POST",
        "/templates",
        json=data,
        idempotency_key=idempotency_key,
        response_model=Template,
    )


async def retrieve_template(client: LobClient, template_id: str) -> Template:
    return await client.request(
        "GET",
        f"/templates/{template_id}",
        response_model=Template,
    )


async def delete_template(client: LobClient, template_id: str) -> Dict[str, Any]:
    return await client.request("DELETE", f"/templates/{template_id}")
