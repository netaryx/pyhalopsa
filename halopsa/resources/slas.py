"""SLAs resource."""

from __future__ import annotations

from typing import Any

from ..models._base import PaginatedResponse
from ..models.sla import SLA
from ._base import CRUDResource


class SLAsResource(CRUDResource[SLA, SLA, SLA]):
    _path = "SLA"
    _list_key = "slas"
    _model = SLA
    _list_model = SLA

    def _parse_list(self, data: Any) -> PaginatedResponse[SLA]:
        if isinstance(data, list):
            items = [self._list_model.model_validate(i) for i in data]
            return PaginatedResponse[SLA](record_count=len(items), items=items)
        return super()._parse_list(data)
