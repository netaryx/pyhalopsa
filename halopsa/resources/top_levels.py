"""TopLevels resource."""

from __future__ import annotations

from typing import Any

from ..models._base import PaginatedResponse
from ..models.top_level import TopLevel
from ._base import CRUDResource


class TopLevelsResource(CRUDResource[TopLevel, TopLevel, TopLevel]):
    _path = "TopLevel"
    _list_key = "toplevels"
    _model = TopLevel
    _list_model = TopLevel

    def _parse_list(self, data: Any) -> PaginatedResponse[TopLevel]:
        if isinstance(data, list):
            items = [self._list_model.model_validate(i) for i in data]
            return PaginatedResponse[TopLevel](record_count=len(items), items=items)
        return super()._parse_list(data)
