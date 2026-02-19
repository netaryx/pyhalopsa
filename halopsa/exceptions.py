"""HaloPSA exception hierarchy."""

from __future__ import annotations


class HaloError(Exception):
    """Base exception for all HaloPSA errors."""


class HaloAPIError(HaloError):
    """Base for HTTP API errors."""

    def __init__(
        self,
        message: str,
        status_code: int,
        response_body: str | None = None,
    ) -> None:
        self.status_code = status_code
        self.response_body = response_body
        super().__init__(message)


class HaloValidationError(HaloAPIError):
    """400 Bad Request."""


class HaloAuthenticationError(HaloAPIError):
    """401 Unauthorized."""


class HaloForbiddenError(HaloAPIError):
    """403 Forbidden."""


class HaloNotFoundError(HaloAPIError):
    """404 Not Found."""


class HaloRateLimitError(HaloAPIError):
    """429 Too Many Requests."""

    def __init__(
        self,
        message: str,
        status_code: int = 429,
        response_body: str | None = None,
        retry_after: float | None = None,
    ) -> None:
        self.retry_after = retry_after
        super().__init__(message, status_code, response_body)


class HaloServerError(HaloAPIError):
    """5xx Server Error."""


class HaloTokenError(HaloError):
    """OAuth2 token fetch failure."""


class HaloTimeoutError(HaloError):
    """Request timeout."""
