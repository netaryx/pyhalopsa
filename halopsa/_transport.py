"""Thin httpx wrappers for sync and async transports."""

from __future__ import annotations

import httpx


class _SyncTransport:
    """Wraps ``httpx.Client``."""

    def __init__(self, *, timeout: float = 30.0) -> None:
        self._client: httpx.Client | None = None
        self._timeout = timeout

    @property
    def client(self) -> httpx.Client:
        if self._client is None or self._client.is_closed:
            self._client = httpx.Client(timeout=self._timeout)
        return self._client

    def send(
        self,
        method: str,
        url: str,
        *,
        headers: dict[str, str] | None = None,
        params: dict | None = None,
        json_body: dict | list | None = None,
        content: bytes | None = None,
        content_type: str | None = None,
    ) -> httpx.Response:
        kw: dict = {
            "method": method,
            "url": url,
            "headers": headers or {},
            "params": params,
        }
        if json_body is not None:
            kw["json"] = json_body
        elif content is not None:
            kw["content"] = content
            if content_type:
                kw["headers"]["Content-Type"] = content_type
        return self.client.request(**kw)

    def close(self) -> None:
        if self._client and not self._client.is_closed:
            self._client.close()


class _AsyncTransport:
    """Wraps ``httpx.AsyncClient``."""

    def __init__(self, *, timeout: float = 30.0) -> None:
        self._client: httpx.AsyncClient | None = None
        self._timeout = timeout

    @property
    def client(self) -> httpx.AsyncClient:
        if self._client is None or self._client.is_closed:
            self._client = httpx.AsyncClient(timeout=self._timeout)
        return self._client

    async def send(
        self,
        method: str,
        url: str,
        *,
        headers: dict[str, str] | None = None,
        params: dict | None = None,
        json_body: dict | list | None = None,
        content: bytes | None = None,
        content_type: str | None = None,
    ) -> httpx.Response:
        kw: dict = {
            "method": method,
            "url": url,
            "headers": headers or {},
            "params": params,
        }
        if json_body is not None:
            kw["json"] = json_body
        elif content is not None:
            kw["content"] = content
            if content_type:
                kw["headers"]["Content-Type"] = content_type
        return await self.client.request(**kw)

    async def close(self) -> None:
        if self._client and not self._client.is_closed:
            await self._client.aclose()
