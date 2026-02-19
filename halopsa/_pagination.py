"""Lazy page iterators for sync and async list_all()."""

from __future__ import annotations

from typing import (
    Any,
    AsyncIterator,
    Callable,
    Coroutine,
    Generic,
    Iterator,
    TypeVar,
)

from .models._base import PaginatedResponse

T = TypeVar("T")


class PageIterator(Generic[T]):
    """Lazily fetches pages and yields individual items (sync)."""

    def __init__(
        self,
        fetch: Callable[..., PaginatedResponse[T]],
        params: dict[str, Any],
        page_size: int = 50,
    ) -> None:
        self._fetch = fetch
        self._params = params
        self._page_size = page_size

    def __iter__(self) -> Iterator[T]:
        page_no = 1
        while True:
            page = self._fetch(
                **self._params,
                page_size=self._page_size,
                page_no=page_no,
            )
            yield from page.items
            if not page.has_next:
                break
            page_no += 1


class AsyncPageIterator(Generic[T]):
    """Lazily fetches pages and yields individual items (async)."""

    def __init__(
        self,
        fetch: Callable[..., Coroutine[Any, Any, PaginatedResponse[T]]],
        params: dict[str, Any],
        page_size: int = 50,
    ) -> None:
        self._fetch = fetch
        self._params = params
        self._page_size = page_size

    async def __aiter__(self) -> AsyncIterator[T]:
        page_no = 1
        while True:
            page = await self._fetch(
                **self._params,
                page_size=self._page_size,
                page_no=page_no,
            )
            for item in page.items:
                yield item
            if not page.has_next:
                break
            page_no += 1
