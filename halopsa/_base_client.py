"""Shared request logic, retry, and error mapping."""

from __future__ import annotations

import time
from typing import Any, TypeVar

import httpx

from .exceptions import (
    HaloAPIError,
    HaloAuthenticationError,
    HaloForbiddenError,
    HaloNotFoundError,
    HaloRateLimitError,
    HaloServerError,
    HaloTimeoutError,
    HaloValidationError,
)

T = TypeVar("T")

_RETRYABLE_STATUS = {429, 500, 502, 503, 504}


class _BaseClientMixin:
    """Shared helpers mixed into both sync and async clients."""

    base_url: str
    max_retries: int
    retry_backoff_factor: float

    def _build_url(self, path: str) -> str:
        path = path.lstrip("/")
        return f"{self.base_url}/api/{path}"

    @staticmethod
    def _clean_params(params: dict[str, Any] | None) -> dict[str, Any] | None:
        if params is None:
            return None
        return {k: v for k, v in params.items() if v is not None}

    @staticmethod
    def _map_error(resp: httpx.Response) -> HaloAPIError:
        code = resp.status_code
        body = resp.text
        msg = f"HaloPSA API error {code}: {body[:500]}"

        if code == 400:
            return HaloValidationError(msg, code, body)
        if code == 401:
            return HaloAuthenticationError(msg, code, body)
        if code == 403:
            return HaloForbiddenError(msg, code, body)
        if code == 404:
            return HaloNotFoundError(msg, code, body)
        if code == 429:
            retry_after = None
            raw = resp.headers.get("Retry-After")
            if raw:
                try:
                    retry_after = float(raw)
                except ValueError:
                    pass
            return HaloRateLimitError(msg, code, body, retry_after=retry_after)
        if code >= 500:
            return HaloServerError(msg, code, body)
        return HaloAPIError(msg, code, body)

    def _should_retry(self, resp: httpx.Response, attempt: int) -> bool:
        return (
            resp.status_code in _RETRYABLE_STATUS
            and attempt < self.max_retries
        )

    def _backoff(self, resp: httpx.Response, attempt: int) -> float:
        if resp.status_code == 429:
            raw = resp.headers.get("Retry-After")
            if raw:
                try:
                    return float(raw)
                except ValueError:
                    pass
        return self.retry_backoff_factor * (2 ** (attempt - 1))

    @staticmethod
    def _sleep_sync(seconds: float) -> None:
        time.sleep(seconds)
