"""Workdays resource."""

from __future__ import annotations

from typing import Any

from ..models._base import PaginatedResponse
from ..models.workday import Workday
from ._base import CRUDResource


class WorkdaysResource(CRUDResource[Workday, Workday, Workday]):
    _path = "Workday"
    _list_key = "workdays"
    _model = Workday
    _list_model = Workday

    def _parse_list(self, data: Any) -> PaginatedResponse[Workday]:
        if isinstance(data, list):
            items = [self._list_model.model_validate(i) for i in data]
            return PaginatedResponse[Workday](record_count=len(items), items=items)
        return super()._parse_list(data)
