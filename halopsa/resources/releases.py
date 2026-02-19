"""Releases resource."""

from __future__ import annotations

from typing import Any

from ..models._base import PaginatedResponse
from ..models.release import Release
from ._base import CRUDResource


class ReleasesResource(CRUDResource[Release, Release, Release]):
    _path = "Release"
    _list_key = "releases"
    _model = Release
    _list_model = Release

    def _parse_list(self, data: Any) -> PaginatedResponse[Release]:
        if isinstance(data, list):
            items = [self._list_model.model_validate(i) for i in data]
            return PaginatedResponse[Release](record_count=len(items), items=items)
        return super()._parse_list(data)

    def list(
        self,
        *,
        page_size: int = 50,
        page_no: int = 1,
        product_id: int | None = None,
        search: str | None = None,
        **params: Any,
    ) -> PaginatedResponse[Release]:
        params.update(
            {k: v for k, v in {
                "product_id": product_id,
                "search": search,
            }.items() if v is not None}
        )
        return super().list(page_size=page_size, page_no=page_no, **params)

    async def alist(
        self,
        *,
        page_size: int = 50,
        page_no: int = 1,
        product_id: int | None = None,
        search: str | None = None,
        **params: Any,
    ) -> PaginatedResponse[Release]:
        params.update(
            {k: v for k, v in {
                "product_id": product_id,
                "search": search,
            }.items() if v is not None}
        )
        return await super().alist(page_size=page_size, page_no=page_no, **params)
