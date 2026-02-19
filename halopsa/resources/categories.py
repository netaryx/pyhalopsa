"""Categories resource."""

from __future__ import annotations

from typing import Any

from ..models._base import PaginatedResponse
from ..models.category import Category
from ._base import CRUDResource


class CategoriesResource(CRUDResource[Category, Category, Category]):
    _path = "Category"
    _list_key = "categories"
    _model = Category
    _list_model = Category

    def _parse_list(self, data: Any) -> PaginatedResponse[Category]:
        if isinstance(data, list):
            items = [self._list_model.model_validate(i) for i in data]
            return PaginatedResponse[Category](record_count=len(items), items=items)
        return super()._parse_list(data)

    def list(
        self,
        *,
        page_size: int = 50,
        page_no: int = 1,
        type_id: int | None = None,
        **params: Any,
    ) -> PaginatedResponse[Category]:
        params.update(
            {k: v for k, v in {
                "type_id": type_id,
            }.items() if v is not None}
        )
        return super().list(page_size=page_size, page_no=page_no, **params)

    async def alist(
        self,
        *,
        page_size: int = 50,
        page_no: int = 1,
        type_id: int | None = None,
        **params: Any,
    ) -> PaginatedResponse[Category]:
        params.update(
            {k: v for k, v in {
                "type_id": type_id,
            }.items() if v is not None}
        )
        return await super().alist(page_size=page_size, page_no=page_no, **params)
