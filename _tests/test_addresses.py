from __future__ import annotations

import pytest

from backend.app.core.third_party_integrations.lob.api import addresses
from backend.app.core.third_party_integrations.lob.api._base import Address, AddressCreate, AddressListResponse, DeleteResponse


@pytest.mark.asyncio
async def test_list_addresses(dummy_client_factory):
    routes = {
        ("GET", "/addresses"): {
            "object": "list",
            "data": [
                {"id": "adr_1", "object": "address", "name": "Ada"},
                {"id": "adr_2", "object": "address", "name": "Alan"},
            ],
            "count": 2,
        }
    }
    client = dummy_client_factory(routes)

    resp = await addresses.list_addresses(client, limit=2)
    assert isinstance(resp, AddressListResponse)
    assert len(resp.data) == 2
    assert resp.count == 2


@pytest.mark.asyncio
async def test_create_address(dummy_client_factory):
    payload = AddressCreate(
        name="Ada",
        address_line1="123 Main",
        address_city="SF",
        address_country="US",
    )
    routes = {
        ("POST", "/addresses"): {
            "id": "adr_1",
            "object": "address",
            "name": "Ada",
            "address_line1": "123 Main",
            "address_city": "SF",
            "address_country": "US",
        }
    }
    client = dummy_client_factory(routes)

    adr = await addresses.create_address(client, data=payload)
    assert isinstance(adr, Address)
    assert adr.id == "adr_1"
    assert adr.name == "Ada"


@pytest.mark.asyncio
async def test_retrieve_address(dummy_client_factory):
    routes = {
        ("GET", "/addresses/adr_1"): {
            "id": "adr_1",
            "object": "address",
            "name": "Ada",
        }
    }
    client = dummy_client_factory(routes)

    adr = await addresses.retrieve_address(client, address_id="adr_1")
    assert isinstance(adr, Address)
    assert adr.id == "adr_1"


@pytest.mark.asyncio
async def test_delete_address(dummy_client_factory):
    routes = {("DELETE", "/addresses/adr_1"): {"id": "adr_1", "deleted": True}}
    client = dummy_client_factory(routes)

    resp = await addresses.delete_address(client, address_id="adr_1")
    assert isinstance(resp, DeleteResponse)
    assert resp.id == "adr_1"
    assert resp.deleted is True
