"""TicketTypes resource."""

from __future__ import annotations

from typing import Any

from ..models._base import PaginatedResponse
from ..models.ticket_type import TicketType
from ._base import CRUDResource


class TicketTypesResource(CRUDResource[TicketType, TicketType, TicketType]):
    _path = "TicketType"
    _list_key = "tickettypes"
    _model = TicketType
    _list_model = TicketType

    def _parse_list(self, data: Any) -> PaginatedResponse[TicketType]:
        if isinstance(data, list):
            items = [self._list_model.model_validate(i) for i in data]
            return PaginatedResponse[TicketType](record_count=len(items), items=items)
        return super()._parse_list(data)
