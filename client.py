from __future__ import annotations

import asyncio
import logging
from typing import Any, Dict, Optional, Type, TypeVar
from urllib.parse import urljoin

import aiohttp
import backoff
from pydantic import BaseModel, ValidationError

from .config import LobConfig, config as default_config

T = TypeVar("T", bound=BaseModel)
logger = logging.getLogger(__name__)


class LobAPIError(Exception):
    def __init__(self, message: str, status_code: Optional[int] = None, response: Optional[Dict[str, Any]] = None):
        super().__init__(message)
        self.status_code = status_code
        self.response = response


class LobAuthError(LobAPIError):
    pass


class LobRateLimitError(LobAPIError):
    def __init__(self, message: str, retry_after: Optional[int] = None, response: Optional[Dict[str, Any]] = None):
        super().__init__(message, status_code=429, response=response)
        self.retry_after = retry_after


class LobClient:
    """
    Async Lob API client.
    - Basic Auth: API key as username, blank password
    - Optional Lob-Version header
    - Optional Idempotency-Key header for create calls
    """
    def __init__(self, cfg: Optional[LobConfig] = None):
        self.config = cfg or default_config
        self._session: Optional[aiohttp.ClientSession] = None
        self._last_request_time = 0.0

    async def __aenter__(self) -> "LobClient":
        await self.start()
        return self

    async def __aexit__(self, *args) -> None:
        await self.close()

    async def start(self) -> None:
        if self._session is None or self._session.closed:
            headers = {"Accept": "application/json"}
            if self.config.api_version:
                headers["Lob-Version"] = self.config.api_version
            timeout = aiohttp.ClientTimeout(total=self.config.timeout)
            self._session = aiohttp.ClientSession(headers=headers, timeout=timeout)

    async def close(self) -> None:
        if self._session and not self._session.closed:
            await self._session.close()

    async def _enforce_min_interval(self) -> None:
        # Basic pacing to avoid hammering
        now = asyncio.get_event_loop().time()
        elapsed = now - self._last_request_time
        if elapsed < 0.05:
            await asyncio.sleep(0.05 - elapsed)
        self._last_request_time = asyncio.get_event_loop().time()

    @backoff.on_exception(
        backoff.expo,
        (aiohttp.ClientError, asyncio.TimeoutError, LobRateLimitError),
        max_tries=lambda self: self.config.max_retries,
        jitter=backoff.full_jitter,
    )
    async def request(
        self,
        method: str,
        endpoint: str,
        *,
        json: Optional[Dict[str, Any]] = None,
        params: Optional[Dict[str, Any]] = None,
        idempotency_key: Optional[str] = None,
        response_model: Optional[Type[T]] = None,
    ) -> T | Dict[str, Any]:
        if self._session is None or self._session.closed:
            await self.start()

        assert self._session is not None

        await self._enforce_min_interval()

        url = urljoin(self.config.base_url.rstrip("/") + "/", endpoint.lstrip("/"))
        headers: Dict[str, str] = {}
        if idempotency_key:
            headers["Idempotency-Key"] = idempotency_key

        auth = aiohttp.BasicAuth(self.config.api_key, "")

        async with self._session.request(
            method=method,
            url=url,
            json=json,
            params=params,
            headers=headers,
            auth=auth,
        ) as resp:
            # Handle status and parse body
            content_type = resp.headers.get("Content-Type", "")
            data: Any
            if "application/json" in content_type:
                data = await resp.json()
            else:
                text = await resp.text()
                data = {"raw": text}

            if resp.status >= 400:
                if resp.status == 401:
                    raise LobAuthError("Unauthorized (check API key)", status_code=401, response=data)
                if resp.status == 429:
                    retry_after = None
                    ra = resp.headers.get("Retry-After")
                    if ra:
                        try:
                            retry_after = int(ra)
                        except ValueError:
                            retry_after = None
                    raise LobRateLimitError("Rate limit exceeded", retry_after=retry_after, response=data)
                raise LobAPIError(f"Lob API error: {data}", status_code=resp.status, response=data)

            # Optionally parse into a Pydantic model
            if response_model is not None:
                try:
                    return response_model.model_validate(data)  # pydantic v2
                except ValidationError as e:
                    raise LobAPIError(f"Failed to parse response: {e}") from e
            return data