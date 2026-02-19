"""Items resource."""

from __future__ import annotations

from typing import Any

from ..models._base import PaginatedResponse
from ..models.item import Item
from ._base import CRUDResource


class ItemsResource(CRUDResource[Item, Item, Item]):
    _path = "Item"
    _list_key = "items"
    _model = Item
    _list_model = Item

    def list(
        self,
        *,
        page_size: int = 50,
        page_no: int = 1,
        search: str | None = None,
        supplier_id: int | None = None,
        assetgroup_id: int | None = None,
        **params: Any,
    ) -> PaginatedResponse[Item]:
        params.update(
            {k: v for k, v in {
                "search": search,
                "supplier_id": supplier_id,
                "assetgroup_id": assetgroup_id,
            }.items() if v is not None}
        )
        return super().list(page_size=page_size, page_no=page_no, **params)

    async def alist(
        self,
        *,
        page_size: int = 50,
        page_no: int = 1,
        search: str | None = None,
        **params: Any,
    ) -> PaginatedResponse[Item]:
        params.update(
            {k: v for k, v in {
                "search": search,
            }.items() if v is not None}
        )
        return await super().alist(page_size=page_size, page_no=page_no, **params)
