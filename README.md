# Lob Python Integration: Async API Client for Lob

[![Python](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

An async-first Lob API integration used by this backend. It provides lightweight wrappers around Lob endpoints with optional typed Pydantic models and automatic retries, auth, and idempotency support.

## Key Features

- Fully async via `aiohttp`
- Basic Auth with API key, optional Lob-Version header
- Idempotency-Key support for create endpoints
- Built-in retries with exponential backoff and rate-limit handling
- Iterative typing using Pydantic models and generic `ListResponse[T]`

## Installation

This lives inside the monorepo. If you need a standalone install, ensure these deps are present:

```toml
# pyproject.toml (excerpt)
[project]
dependencies = [
  "aiohttp>=3.9",
  "backoff>=2.2",
  "pydantic>=2.5",
]
```

## Configuration

See `backend/app/core/third_party_integrations/lob/config.py` for defaults.

- `LOB_API_KEY` (required)
- `LOB_BASE_URL` (default: `https://api.lob.com`)
- `LOB_API_VERSION` (optional)
- `LOB_TIMEOUT` (seconds)
- `LOB_MAX_RETRIES`

## Quick Start

```python
from backend.app.core.third_party_integrations.lob import LobClient
from backend.app.core.third_party_integrations.lob.api import postcards

async def main():
    async with LobClient() as client:
        pc = await postcards.create_postcard(
            client,
            data={
                "to": {"name": "Jane", "address_line1": "185 Berry St", "address_city": "SF", "address_state": "CA", "address_zip": "94107"},
                "from": {"name": "ACME", "address_line1": "123 Main St", "address_city": "SF", "address_state": "CA", "address_zip": "94105"},
                "front": "https://example.com/front.pdf",
                "back": "https://example.com/back.pdf",
            },
            idempotency_key="unique-key-123",
        )
        print(pc.id)
```

## Typed Endpoints (initial set)

- Postcards: list/create/retrieve (typed), cancel (raw)
- Letters: list/create/retrieve (typed), cancel (raw)
- Self Mailers: list/create/retrieve (typed), cancel (raw)
- Templates: list/create/retrieve (typed), delete (raw)
- Template Versions: list/create/retrieve (typed)
- Webhooks: list/create/retrieve (typed), delete (raw)

All other endpoints are implemented and currently return raw dicts; they will be typed iteratively.

## Error Handling

`LobClient.request()` raises specific errors on non-2xx responses:

- Auth: 401 -> `LobAuthError`
- Rate limit: 429 -> `LobRateLimitError` (with `retry_after` when available)
- Other: `LobAPIError`

## Development

- Core client: `backend/app/core/third_party_integrations/lob/client.py`
- Endpoints: `backend/app/core/third_party_integrations/lob/api/`
- Models: `backend/app/core/third_party_integrations/lob/api/_models.py`
- List wrapper: `backend/app/core/third_party_integrations/lob/api/_responses.py`

---

Legacy notes below (ManyChat SDK – kept for historical scaffolding reference):