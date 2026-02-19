"""Reports resource."""

from __future__ import annotations

from typing import Any

from ..models._base import PaginatedResponse
from ..models.report import Report
from ._base import CRUDResource


class ReportsResource(CRUDResource[Report, Report, Report]):
    _path = "Report"
    _list_key = "reports"
    _model = Report
    _list_model = Report

    def list(
        self,
        *,
        page_size: int = 50,
        page_no: int = 1,
        search: str | None = None,
        **params: Any,
    ) -> PaginatedResponse[Report]:
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
    ) -> PaginatedResponse[Report]:
        params.update(
            {k: v for k, v in {
                "search": search,
            }.items() if v is not None}
        )
        return await super().alist(page_size=page_size, page_no=page_no, **params)
