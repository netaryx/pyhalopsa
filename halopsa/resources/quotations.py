"""Quotations resource."""

from __future__ import annotations

from typing import Any

from ..models._base import PaginatedResponse
from ..models.quotation import Quotation
from ._base import CRUDResource


class QuotationsResource(CRUDResource[Quotation, Quotation, Quotation]):
    _path = "Quotation"
    _list_key = "quotes"
    _model = Quotation
    _list_model = Quotation

    def list(
        self,
        *,
        page_size: int = 50,
        page_no: int = 1,
        client_id: int | None = None,
        ticket_id: int | None = None,
        search: str | None = None,
        **params: Any,
    ) -> PaginatedResponse[Quotation]:
        params.update(
            {k: v for k, v in {
                "client_id": client_id,
                "ticket_id": ticket_id,
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
        ticket_id: int | None = None,
        **params: Any,
    ) -> PaginatedResponse[Quotation]:
        params.update(
            {k: v for k, v in {
                "client_id": client_id,
                "ticket_id": ticket_id,
            }.items() if v is not None}
        )
        return await super().alist(page_size=page_size, page_no=page_no, **params)
