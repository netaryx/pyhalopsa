"""Timesheets resource."""

from __future__ import annotations

from typing import Any

from ..models._base import PaginatedResponse
from ..models.timesheet import Timesheet
from ._base import CRUDResource


class TimesheetsResource(CRUDResource[Timesheet, Timesheet, Timesheet]):
    _path = "Timesheet"
    _list_key = "timesheets"
    _model = Timesheet
    _list_model = Timesheet

    def _parse_list(self, data: Any) -> PaginatedResponse[Timesheet]:
        if isinstance(data, list):
            items = [self._list_model.model_validate(i) for i in data]
            return PaginatedResponse[Timesheet](record_count=len(items), items=items)
        return super()._parse_list(data)

    def list(
        self,
        *,
        page_size: int = 50,
        page_no: int = 1,
        agent_id: int | None = None,
        start_date: str | None = None,
        end_date: str | None = None,
        **params: Any,
    ) -> PaginatedResponse[Timesheet]:
        params.update(
            {k: v for k, v in {
                "agent_id": agent_id,
                "start_date": start_date,
                "end_date": end_date,
            }.items() if v is not None}
        )
        return super().list(page_size=page_size, page_no=page_no, **params)

    async def alist(
        self,
        *,
        page_size: int = 50,
        page_no: int = 1,
        agent_id: int | None = None,
        **params: Any,
    ) -> PaginatedResponse[Timesheet]:
        params.update(
            {k: v for k, v in {
                "agent_id": agent_id,
            }.items() if v is not None}
        )
        return await super().alist(page_size=page_size, page_no=page_no, **params)

    def delete(self, id: int, **params: Any) -> None:
        raise NotImplementedError("The Timesheet endpoint does not support DELETE")

    async def adelete(self, id: int, **params: Any) -> None:
        raise NotImplementedError("The Timesheet endpoint does not support DELETE")
