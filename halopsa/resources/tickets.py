"""Tickets resource."""

from __future__ import annotations

from typing import Any

from ..models._base import PaginatedResponse
from ..models.ticket import Ticket, TicketList
from .._pagination import PageIterator, AsyncPageIterator
from ._base import CRUDResource


class TicketsResource(CRUDResource[Ticket, TicketList, TicketList]):
    _path = "Tickets"
    _list_key = "tickets"
    _model = Ticket
    _list_model = TicketList

    def list(
        self,
        *,
        page_size: int = 50,
        page_no: int = 1,
        client_id: int | None = None,
        site_id: int | None = None,
        user_id: int | None = None,
        agent_id: int | None = None,
        team_id: int | None = None,
        status_id: int | None = None,
        tickettype_id: int | None = None,
        priority_id: int | None = None,
        sla_id: int | None = None,
        category_1: str | None = None,
        category_2: str | None = None,
        category_3: str | None = None,
        category_4: str | None = None,
        open_only: bool | None = None,
        closedonly: bool | None = None,
        search: str | None = None,
        order: str | None = None,
        orderdesc: bool | None = None,
        asset_id: int | None = None,
        contract_id: int | None = None,
        **params: Any,
    ) -> PaginatedResponse[TicketList]:
        params.update(
            {k: v for k, v in {
                "client_id": client_id,
                "site_id": site_id,
                "user_id": user_id,
                "agent_id": agent_id,
                "team_id": team_id,
                "status_id": status_id,
                "tickettype_id": tickettype_id,
                "priority_id": priority_id,
                "sla_id": sla_id,
                "category_1": category_1,
                "category_2": category_2,
                "category_3": category_3,
                "category_4": category_4,
                "open_only": open_only,
                "closedonly": closedonly,
                "search": search,
                "order": order,
                "orderdesc": orderdesc,
                "asset_id": asset_id,
                "contract_id": contract_id,
            }.items() if v is not None}
        )
        return super().list(page_size=page_size, page_no=page_no, **params)

    async def alist(
        self,
        *,
        page_size: int = 50,
        page_no: int = 1,
        client_id: int | None = None,
        site_id: int | None = None,
        user_id: int | None = None,
        agent_id: int | None = None,
        team_id: int | None = None,
        status_id: int | None = None,
        open_only: bool | None = None,
        search: str | None = None,
        **params: Any,
    ) -> PaginatedResponse[TicketList]:
        params.update(
            {k: v for k, v in {
                "client_id": client_id,
                "site_id": site_id,
                "user_id": user_id,
                "agent_id": agent_id,
                "team_id": team_id,
                "status_id": status_id,
                "open_only": open_only,
                "search": search,
            }.items() if v is not None}
        )
        return await super().alist(page_size=page_size, page_no=page_no, **params)
