"""Invoices resource."""

from __future__ import annotations

from typing import Any

from ..models._base import PaginatedResponse
from ..models.invoice import Invoice
from ._base import CRUDResource


class InvoicesResource(CRUDResource[Invoice, Invoice, Invoice]):
    _path = "Invoice"
    _list_key = "invoices"
    _model = Invoice
    _list_model = Invoice

    def list(
        self,
        *,
        page_size: int = 50,
        page_no: int = 1,
        client_id: int | None = None,
        posted: bool | None = None,
        search: str | None = None,
        **params: Any,
    ) -> PaginatedResponse[Invoice]:
        params.update(
            {k: v for k, v in {
                "client_id": client_id,
                "posted": posted,
                "search": search,
            }.items() if v is not None}
        )
        return super().list(page_size=page_size, page_no=page_no, **params)

    async def alist(
        self,
        *,
        page_size: int = 50,
        page_no: int = 1,
        client_id: int | None = None,
        posted: bool | None = None,
        search: str | None = None,
        **params: Any,
    ) -> PaginatedResponse[Invoice]:
        params.update(
            {k: v for k, v in {
                "client_id": client_id,
                "posted": posted,
                "search": search,
            }.items() if v is not None}
        )
        return await super().alist(page_size=page_size, page_no=page_no, **params)
