from __future__ import annotations

from typing import Any, Dict, Optional

from ..client import LobClient
from ._requests import PaginationQuery


async def list_bank_accounts(
    client: LobClient,
    *,
    pagination: Optional[PaginationQuery] = None,
) -> Dict[str, Any]:
    params = pagination.to_params() if pagination else {}
    return await client.request("GET", "/bank_accounts", params=params)


async def create_bank_account(
    client: LobClient,
    data: Dict[str, Any],
) -> Dict[str, Any]:
    return await client.request("POST", "/bank_accounts", json=data)


async def retrieve_bank_account(client: LobClient, bank_id: str) -> Dict[str, Any]:
    return await client.request("GET", f"/bank_accounts/{bank_id}")


async def delete_bank_account(client: LobClient, bank_id: str) -> Dict[str, Any]:
    return await client.request("DELETE", f"/bank_accounts/{bank_id}")
