from __future__ import annotations

from typing import Any, Dict, Optional

from ..client import LobClient
from ._requests import PaginationQuery
from ._responses import ListResponse
from ._models import TemplateVersion


async def list_template_versions(
    client: LobClient,
    template_id: str,
    *,
    pagination: Optional[PaginationQuery] = None,
) -> ListResponse[TemplateVersion]:
    params = pagination.to_params() if pagination else {}
    return await client.request(
        "GET",
        f"/templates/{template_id}/versions",
        params=params,
        response_model=ListResponse[TemplateVersion],
    )


async def create_template_version(
    client: LobClient,
    template_id: str,
    data: Dict[str, Any],
    *,
    idempotency_key: Optional[str] = None,
) -> TemplateVersion:
    return await client.request(
        "POST",
        f"/templates/{template_id}/versions",
        json=data,
        idempotency_key=idempotency_key,
        response_model=TemplateVersion,
    )


async def retrieve_template_version(
    client: LobClient,
    template_id: str,
    version_id: str,
) -> TemplateVersion:
    return await client.request(
        "GET",
        f"/templates/{template_id}/versions/{version_id}",
        response_model=TemplateVersion,
    )
