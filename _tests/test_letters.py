from __future__ import annotations

import pytest

from backend.app.core.third_party_integrations.lob.api import letters
from backend.app.core.third_party_integrations.lob.api._responses import ListResponse
from backend.app.core.third_party_integrations.lob.api._models import Letter


@pytest.mark.asyncio
async def test_list_letters(dummy_client_factory):
    routes = {
        ("GET", "/letters"): {
            "data": [
                {"id": "ltr_1", "object": "letter", "description": "Test 1"},
                {"id": "ltr_2", "object": "letter", "description": "Test 2"},
            ],
            "object": "list",
            "count": 2,
        }
    }
    client = dummy_client_factory(routes)

    resp = await letters.list_letters(client)
    assert isinstance(resp, ListResponse)
    assert len(resp.data) == 2
    assert resp.data[0].id == "ltr_1"


@pytest.mark.asyncio
async def test_create_letter(dummy_client_factory):
    routes = {
        ("POST", "/letters"): {
            "id": "ltr_1",
            "object": "letter",
            "description": "Created",
        }
    }
    client = dummy_client_factory(routes)

    ltr = await letters.create_letter(client, data={"description": "Created"})
    assert isinstance(ltr, Letter)
    assert ltr.id == "ltr_1"


@pytest.mark.asyncio
async def test_retrieve_letter(dummy_client_factory):
    routes = {("GET", "/letters/ltr_1"): {"id": "ltr_1", "object": "letter"}}
    client = dummy_client_factory(routes)

    ltr = await letters.retrieve_letter(client, letter_id="ltr_1")
    assert isinstance(ltr, Letter)
    assert ltr.id == "ltr_1"


@pytest.mark.asyncio
async def test_cancel_letter(dummy_client_factory):
    routes = {("DELETE", "/letters/ltr_1"): {"deleted": True}}
    client = dummy_client_factory(routes)

    resp = await letters.cancel_letter(client, letter_id="ltr_1")
    assert resp["deleted"] is True
