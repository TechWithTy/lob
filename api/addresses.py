from __future__ import annotations

from typing import Any, Dict, Optional

from ..client import LobClient
from ._base import Address, AddressCreate, AddressListResponse, DeleteResponse


async def list_addresses(
    client: LobClient,
    *,
    limit: Optional[int] = None,
    before: Optional[str] = None,
    after: Optional[str] = None,
    include: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
) -> AddressListResponse:
    """List addresses.

    Docs: https://docs.lob.com/#tag/Addresses/operation/addresses_list
    """
    params: Dict[str, Any] = {}
    if limit is not None:
        params["limit"] = limit
    if before:
        params["before"] = before
    if after:
        params["after"] = after
    if include:
        params["include"] = include
    # metadata filters become metadata[key]=value query params
    if metadata:
        for k, v in metadata.items():
            params[f"metadata[{k}]"] = v

    return await client.request(
        "GET",
        "/addresses",
        params=params,
        response_model=AddressListResponse,
    )


async def create_address(
    client: LobClient,
    data: AddressCreate,
    *,
    idempotency_key: Optional[str] = None,
) -> Address:
    """Create an address.

    Docs: https://docs.lob.com/#tag/Addresses/operation/address_create
    """
    return await client.request(
        "POST",
        "/addresses",
        json=data.model_dump(exclude_none=True),
        idempotency_key=idempotency_key,
        response_model=Address,
    )


async def retrieve_address(client: LobClient, address_id: str) -> Address:
    """Retrieve a single address by id."""
    return await client.request(
        "GET",
        f"/addresses/{address_id}",
        response_model=Address,
    )


async def delete_address(client: LobClient, address_id: str) -> DeleteResponse:
    """Delete an address by id."""
    return await client.request(
        "DELETE",
        f"/addresses/{address_id}",
        response_model=DeleteResponse,
    )
