"""Priorities resource."""

from __future__ import annotations

from typing import Any

from ..models._base import PaginatedResponse
from ..models.priority import Priority
from ._base import CRUDResource


class PrioritiesResource(CRUDResource[Priority, Priority, Priority]):
    _path = "Priority"
    _list_key = "priorities"
    _model = Priority
    _list_model = Priority

    def _parse_list(self, data: Any) -> PaginatedResponse[Priority]:
        if isinstance(data, list):
            items = [self._list_model.model_validate(i) for i in data]
            return PaginatedResponse[Priority](record_count=len(items), items=items)
        return super()._parse_list(data)
