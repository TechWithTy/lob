from __future__ import annotations

from typing import Any, Dict, Optional

from ..client import LobClient
from ._requests import PaginationQuery


async def list_uploads(
    client: LobClient,
    *,
    pagination: Optional[PaginationQuery] = None,
) -> Dict[str, Any]:
    params = pagination.to_params() if pagination else {}
    return await client.request("GET", "/uploads", params=params)


async def create_upload(
    client: LobClient,
    data: Dict[str, Any],
    *,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    return await client.request(
        "POST", "/uploads", json=data, idempotency_key=idempotency_key
    )


async def retrieve_upload(client: LobClient, upload_id: str) -> Dict[str, Any]:
    return await client.request("GET", f"/uploads/{upload_id}")


async def delete_upload(client: LobClient, upload_id: str) -> Dict[str, Any]:
    return await client.request("DELETE", f"/uploads/{upload_id}")
