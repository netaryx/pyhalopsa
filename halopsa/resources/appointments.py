"""Appointments resource."""

from __future__ import annotations

from typing import Any

from ..models._base import PaginatedResponse
from ..models.appointment import Appointment
from ._base import CRUDResource


class AppointmentsResource(CRUDResource[Appointment, Appointment, Appointment]):
    _path = "Appointment"
    _list_key = "appointments"
    _model = Appointment
    _list_model = Appointment

    def list(
        self,
        *,
        page_size: int = 50,
        page_no: int = 1,
        agent_id: int | None = None,
        ticket_id: int | None = None,
        search: str | None = None,
        start: str | None = None,
        end: str | None = None,
        **params: Any,
    ) -> PaginatedResponse[Appointment]:
        params.update(
            {k: v for k, v in {
                "agent_id": agent_id,
                "ticket_id": ticket_id,
                "search": search,
                "start": start,
                "end": end,
            }.items() if v is not None}
        )
        return super().list(page_size=page_size, page_no=page_no, **params)

    async def alist(
        self,
        *,
        page_size: int = 50,
        page_no: int = 1,
        agent_id: int | None = None,
        ticket_id: int | None = None,
        **params: Any,
    ) -> PaginatedResponse[Appointment]:
        params.update(
            {k: v for k, v in {
                "agent_id": agent_id,
                "ticket_id": ticket_id,
            }.items() if v is not None}
        )
        return await super().alist(page_size=page_size, page_no=page_no, **params)
