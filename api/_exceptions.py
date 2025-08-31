from __future__ import annotations

from typing import Any, Dict, Optional


class LobError(Exception):
    """Base class for all Lob SDK errors."""


class LobAPIError(LobError):
    """Generic API error wrapper with optional HTTP status and response body."""

    def __init__(self, message: str, *, status_code: Optional[int] = None, response: Optional[Dict[str, Any]] = None):
        super().__init__(message)
        self.status_code = status_code
        self.response = response


class LobAuthError(LobAPIError):
    """401 Unauthorized or authentication-related issues."""


class LobRateLimitError(LobAPIError):
    """429 Too Many Requests. Includes optional retry_after seconds."""

    def __init__(self, message: str, *, retry_after: Optional[int] = None, response: Optional[Dict[str, Any]] = None):
        super().__init__(message, status_code=429, response=response)
        self.retry_after = retry_after


class LobValidationError(LobAPIError):
    """400 Bad Request validation or schema issues."""


class LobNotFoundError(LobAPIError):
    """404 Not Found for a given resource id."""


class LobConflictError(LobAPIError):
    """409 Conflict, e.g. idempotency conflicts."""


class LobServerError(LobAPIError):
    """5xx server-side error."""


class LobTimeoutError(LobError):
    """Client-side request timeout occurred."""


class LobConnectionError(LobError):
    """Network connectivity/transport error."""


class LobRetryError(LobError):
    """Raised after exhausting retry attempts."""
