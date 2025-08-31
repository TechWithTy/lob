from __future__ import annotations

from typing import Any, Dict, Optional

from ..client import LobClient
from ._requests import PaginationQuery


async def list_buckslips(
    client: LobClient,
    *,
    pagination: Optional[PaginationQuery] = None,
) -> Dict[str, Any]:
    params = pagination.to_params() if pagination else {}
    return await client.request("GET", "/buckslips", params=params)


async def create_buckslip(
    client: LobClient,
    data: Dict[str, Any],
    *,
    idempotency_key: Optional[str] = None,
) -> Dict[str, Any]:
    return await client.request(
        "POST", "/buckslips", json=data, idempotency_key=idempotency_key
    )


async def retrieve_buckslip(client: LobClient, buckslip_id: str) -> Dict[str, Any]:
    return await client.request("GET", f"/buckslips/{buckslip_id}")


async def delete_buckslip(client: LobClient, buckslip_id: str) -> Dict[str, Any]:
    return await client.request("DELETE", f"/buckslips/{buckslip_id}")
