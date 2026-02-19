"""OAuth2 client_credentials token management."""

from __future__ import annotations

import asyncio
import threading
import time
from dataclasses import dataclass, field

import httpx

from .exceptions import HaloTokenError

_REFRESH_MARGIN_SECONDS = 60


@dataclass
class _TokenData:
    access_token: str = ""
    expires_at: float = 0.0

    @property
    def is_valid(self) -> bool:
        return bool(self.access_token) and time.time() < (
            self.expires_at - _REFRESH_MARGIN_SECONDS
        )


class TokenManager:
    """Thread-safe / async-safe OAuth2 client_credentials token manager."""

    def __init__(
        self,
        token_url: str,
        client_id: str,
        client_secret: str,
        scope: str = "all",
        tenant: str | None = None,
    ) -> None:
        self._token_url = token_url
        self._client_id = client_id
        self._client_secret = client_secret
        self._scope = scope
        self._tenant = tenant
        self._token = _TokenData()
        self._sync_lock = threading.Lock()
        self._async_lock: asyncio.Lock | None = None

    def _build_form(self) -> dict[str, str]:
        data: dict[str, str] = {
            "grant_type": "client_credentials",
            "client_id": self._client_id,
            "client_secret": self._client_secret,
            "scope": self._scope,
        }
        if self._tenant:
            data["tenant"] = self._tenant
        return data

    def _parse_response(self, resp: httpx.Response) -> _TokenData:
        if resp.status_code != 200:
            raise HaloTokenError(
                f"Token request failed ({resp.status_code}): {resp.text}"
            )
        body = resp.json()
        return _TokenData(
            access_token=body["access_token"],
            expires_at=time.time() + body.get("expires_in", 3600),
        )

    # ── Sync ──────────────────────────────────────────────────────────

    def get_token(self, http_client: httpx.Client | None = None) -> str:
        if self._token.is_valid:
            return self._token.access_token
        with self._sync_lock:
            if self._token.is_valid:
                return self._token.access_token
            return self._refresh_sync(http_client)

    def force_refresh(self, http_client: httpx.Client | None = None) -> str:
        with self._sync_lock:
            return self._refresh_sync(http_client)

    def _refresh_sync(self, http_client: httpx.Client | None = None) -> str:
        close_after = False
        if http_client is None:
            http_client = httpx.Client()
            close_after = True
        try:
            resp = http_client.post(self._token_url, data=self._build_form())
            self._token = self._parse_response(resp)
            return self._token.access_token
        finally:
            if close_after:
                http_client.close()

    # ── Async ─────────────────────────────────────────────────────────

    async def aget_token(
        self, http_client: httpx.AsyncClient | None = None
    ) -> str:
        if self._token.is_valid:
            return self._token.access_token
        lock = self._get_async_lock()
        async with lock:
            if self._token.is_valid:
                return self._token.access_token
            return await self._refresh_async(http_client)

    async def aforce_refresh(
        self, http_client: httpx.AsyncClient | None = None
    ) -> str:
        lock = self._get_async_lock()
        async with lock:
            return await self._refresh_async(http_client)

    async def _refresh_async(
        self, http_client: httpx.AsyncClient | None = None
    ) -> str:
        close_after = False
        if http_client is None:
            http_client = httpx.AsyncClient()
            close_after = True
        try:
            resp = await http_client.post(
                self._token_url, data=self._build_form()
            )
            self._token = self._parse_response(resp)
            return self._token.access_token
        finally:
            if close_after:
                await http_client.aclose()

    def _get_async_lock(self) -> asyncio.Lock:
        if self._async_lock is None:
            self._async_lock = asyncio.Lock()
        return self._async_lock

    def invalidate(self) -> None:
        """Force the next call to fetch a fresh token."""
        self._token = _TokenData()
