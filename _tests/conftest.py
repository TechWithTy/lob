from __future__ import annotations

from typing import Any, Dict, Optional, Tuple

import pytest


class DummyClient:
    """Minimal dummy Lob client that mimics LobClient.request().

    Supports response_model parsing to typed Pydantic models just like
    the real client so API functions can be tested in isolation.
    """

    def __init__(self, routes: Dict[Tuple[str, str], Dict[str, Any]]):
        # key: (METHOD, endpoint) -> payload
        self._routes = routes

    async def request(
        self,
        method: str,
        endpoint: str,
        *,
        json: Optional[Dict[str, Any]] = None,
        params: Optional[Dict[str, Any]] = None,
        idempotency_key: Optional[str] = None,
        response_model: Optional[Any] = None,
    ) -> Any:
        payload = self._routes.get((method.upper(), endpoint))
        if payload is None:
            raise AssertionError(f"No dummy route for {method} {endpoint}")
        if response_model is not None:
            return response_model.model_validate(payload)
        return payload


@pytest.fixture
def dummy_client_factory():
    def _factory(routes: Dict[Tuple[str, str], Dict[str, Any]]) -> DummyClient:
        return DummyClient(routes)

    return _factory
