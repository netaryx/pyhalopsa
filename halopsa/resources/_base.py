"""Generic CRUD resource base class."""

from __future__ import annotations

from typing import (
    TYPE_CHECKING,
    Any,
    Generic,
    TypeVar,
    get_args,
    get_origin,
)

from ..models._base import HaloModel, PaginatedResponse
from .._pagination import AsyncPageIterator, PageIterator

if TYPE_CHECKING:
    from ..client import AsyncHaloClient, HaloClient

M = TypeVar("M", bound=HaloModel)  # detail model
L = TypeVar("L", bound=HaloModel)  # list model
V = TypeVar("V", bound=HaloModel)  # view/summary model (often same as L)


class CRUDResource(Generic[M, L, V]):
    """Base providing standard CRUD operations for a HaloPSA resource.

    Subclasses must set:
        _path:        API path segment (e.g. "Tickets")
        _list_key:    JSON key containing the items array (e.g. "tickets")
        _model:       Detail Pydantic model class
        _list_model:  List Pydantic model class
    """

    _path: str
    _list_key: str
    _model: type[M]
    _list_model: type[L]

    def __init__(self, client: HaloClient | AsyncHaloClient) -> None:
        self._client = client

    # ── Sync ──────────────────────────────────────────────────────────

    def list(self, *, page_size: int = 50, page_no: int = 1, **params: Any) -> PaginatedResponse[L]:
        """Fetch a single page of results."""
        params["page_size"] = page_size
        params["page_no"] = page_no
        params["pageinate"] = True
        data = self._client.request("GET", self._path, params=params)
        return self._parse_list(data)

    def list_all(self, *, page_size: int = 50, **params: Any) -> PageIterator[L]:
        """Return a lazy iterator that auto-paginates through all items."""
        return PageIterator(fetch=self.list, params=params, page_size=page_size)

    def get(self, id: int, **params: Any) -> M:
        """Fetch a single resource by ID."""
        data = self._client.request("GET", f"{self._path}/{id}", params=params)
        return self._model.model_validate(data)

    def create(self, item: M | dict[str, Any], **kwargs: Any) -> M:
        """Create a new resource (POST without id)."""
        body = self._to_body(item)
        body.pop("id", None)
        data = self._client.request("POST", self._path, json_body=[body])
        return self._parse_single(data)

    def update(self, item: M | dict[str, Any], **kwargs: Any) -> M:
        """Update an existing resource (POST with id)."""
        body = self._to_body(item)
        if not body.get("id"):
            raise ValueError("update() requires an 'id' field on the model")
        data = self._client.request("POST", self._path, json_body=[body])
        return self._parse_single(data)

    def delete(self, id: int, **params: Any) -> None:
        """Delete a resource by ID."""
        self._client.request("DELETE", f"{self._path}/{id}", params=params)

    def batch_create(self, items: list[M | dict[str, Any]]) -> list[M]:
        """Create multiple resources in a single POST."""
        bodies = [self._to_body(i) for i in items]
        for b in bodies:
            b.pop("id", None)
        data = self._client.request("POST", self._path, json_body=bodies)
        return self._parse_multiple(data)

    # ── Async ─────────────────────────────────────────────────────────

    async def alist(self, *, page_size: int = 50, page_no: int = 1, **params: Any) -> PaginatedResponse[L]:
        params["page_size"] = page_size
        params["page_no"] = page_no
        params["pageinate"] = True
        data = await self._client.arequest("GET", self._path, params=params)
        return self._parse_list(data)

    def alist_all(self, *, page_size: int = 50, **params: Any) -> AsyncPageIterator[L]:
        return AsyncPageIterator(fetch=self.alist, params=params, page_size=page_size)

    async def aget(self, id: int, **params: Any) -> M:
        data = await self._client.arequest("GET", f"{self._path}/{id}", params=params)
        return self._model.model_validate(data)

    async def acreate(self, item: M | dict[str, Any], **kwargs: Any) -> M:
        body = self._to_body(item)
        body.pop("id", None)
        data = await self._client.arequest("POST", self._path, json_body=[body])
        return self._parse_single(data)

    async def aupdate(self, item: M | dict[str, Any], **kwargs: Any) -> M:
        body = self._to_body(item)
        if not body.get("id"):
            raise ValueError("update() requires an 'id' field on the model")
        data = await self._client.arequest("POST", self._path, json_body=[body])
        return self._parse_single(data)

    async def adelete(self, id: int, **params: Any) -> None:
        await self._client.arequest("DELETE", f"{self._path}/{id}", params=params)

    async def abatch_create(self, items: list[M | dict[str, Any]]) -> list[M]:
        bodies = [self._to_body(i) for i in items]
        for b in bodies:
            b.pop("id", None)
        data = await self._client.arequest("POST", self._path, json_body=bodies)
        return self._parse_multiple(data)

    # ── Parsing helpers ───────────────────────────────────────────────

    def _parse_list(self, data: Any) -> PaginatedResponse[L]:
        if isinstance(data, dict):
            items_raw = data.get(self._list_key, [])
            items = [self._list_model.model_validate(i) for i in items_raw]
            return PaginatedResponse[L](
                record_count=data.get("record_count", len(items)),
                items=items,
                page_no=data.get("page_no", 1),
                page_size=data.get("page_size", 50),
            )
        # Fallback: raw list
        items = [self._list_model.model_validate(i) for i in (data or [])]
        return PaginatedResponse[L](record_count=len(items), items=items)

    def _parse_single(self, data: Any) -> M:
        if isinstance(data, list) and data:
            return self._model.model_validate(data[0])
        if isinstance(data, dict):
            return self._model.model_validate(data)
        raise ValueError(f"Unexpected response shape: {type(data)}")

    def _parse_multiple(self, data: Any) -> list[M]:
        if isinstance(data, list):
            return [self._model.model_validate(i) for i in data]
        raise ValueError(f"Unexpected response shape: {type(data)}")

    @staticmethod
    def _to_body(item: HaloModel | dict[str, Any]) -> dict[str, Any]:
        if isinstance(item, HaloModel):
            return item.model_dump(exclude_none=True, by_alias=True)
        return dict(item)
