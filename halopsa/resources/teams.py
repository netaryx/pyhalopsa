"""Teams resource."""

from __future__ import annotations

from typing import Any

from ..models._base import PaginatedResponse
from ..models.team import Team
from ._base import CRUDResource


class TeamsResource(CRUDResource[Team, Team, Team]):
    _path = "Team"
    _list_key = "teams"
    _model = Team
    _list_model = Team

    def _parse_list(self, data: Any) -> PaginatedResponse[Team]:
        if isinstance(data, list):
            items = [self._list_model.model_validate(i) for i in data]
            return PaginatedResponse[Team](record_count=len(items), items=items)
        return super()._parse_list(data)
