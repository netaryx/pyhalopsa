"""Suppliers resource."""

from __future__ import annotations

from typing import Any

from ..models._base import PaginatedResponse
from ..models.supplier import Supplier, SupplierList
from ._base import CRUDResource


class SuppliersResource(CRUDResource[Supplier, SupplierList, SupplierList]):
    _path = "Supplier"
    _list_key = "suppliers"
    _model = Supplier
    _list_model = SupplierList

    def list(
        self,
        *,
        page_size: int = 50,
        page_no: int = 1,
        search: str | None = None,
        **params: Any,
    ) -> PaginatedResponse[SupplierList]:
        params.update(
            {k: v for k, v in {
                "search": search,
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
    ) -> PaginatedResponse[SupplierList]:
        params.update(
            {k: v for k, v in {
                "search": search,
            }.items() if v is not None}
        )
        return await super().alist(page_size=page_size, page_no=page_no, **params)
