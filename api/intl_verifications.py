from __future__ import annotations

from typing import Any, Dict, List, Optional

from ..client import LobClient


async def verify_intl_address(
    client: LobClient,
    data: Dict[str, Any],
) -> Dict[str, Any]:
    return await client.request("POST", "/intl_verifications", json=data)


async def verify_intl_bulk(
    client: LobClient,
    addresses: List[Dict[str, Any]],
) -> Dict[str, Any]:
    return await client.request(
        "POST", "/intl_verifications/bulk", json={"addresses": addresses}
    )
