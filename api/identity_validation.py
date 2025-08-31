from __future__ import annotations

from typing import Any, Dict

from ..client import LobClient


async def validate_identity(
    client: LobClient,
    data: Dict[str, Any],
) -> Dict[str, Any]:
    return await client.request("POST", "/identity_validation", json=data)
