"""Statuses resource."""

from __future__ import annotations

from typing import Any

from ..models._base import PaginatedResponse
from ..models.status import Status
from ._base import CRUDResource


class StatusesResource(CRUDResource[Status, Status, Status]):
    _path = "Status"
    _list_key = "statuses"
    _model = Status
    _list_model = Status

    def _parse_list(self, data: Any) -> PaginatedResponse[Status]:
        if isinstance(data, list):
            items = [self._list_model.model_validate(i) for i in data]
            return PaginatedResponse[Status](record_count=len(items), items=items)
        return super()._parse_list(data)

    def list(
        self,
        *,
        page_size: int = 50,
        page_no: int = 1,
        type: str | None = None,
        **params: Any,
    ) -> PaginatedResponse[Status]:
        params.update(
            {k: v for k, v in {
                "type": type,
            }.items() if v is not None}
        )
        return super().list(page_size=page_size, page_no=page_no, **params)

    async def alist(
        self,
        *,
        page_size: int = 50,
        page_no: int = 1,
        type: str | None = None,
        **params: Any,
    ) -> PaginatedResponse[Status]:
        params.update(
            {k: v for k, v in {
                "type": type,
            }.items() if v is not None}
        )
        return await super().alist(page_size=page_size, page_no=page_no, **params)
