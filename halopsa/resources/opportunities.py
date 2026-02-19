"""Opportunities resource."""

from __future__ import annotations

from typing import Any

from ..models._base import PaginatedResponse
from ..models.opportunity import Opportunity
from ._base import CRUDResource


class OpportunitiesResource(CRUDResource[Opportunity, Opportunity, Opportunity]):
    _path = "Opportunities"
    _list_key = "tickets"
    _model = Opportunity
    _list_model = Opportunity

    def list(
        self,
        *,
        page_size: int = 50,
        page_no: int = 1,
        client_id: int | None = None,
        agent_id: int | None = None,
        search: str | None = None,
        **params: Any,
    ) -> PaginatedResponse[Opportunity]:
        params.update(
            {k: v for k, v in {
                "client_id": client_id,
                "agent_id": agent_id,
                "search": search,
            }.items() if v is not None}
        )
        return super().list(page_size=page_size, page_no=page_no, **params)

    async def alist(
        self,
        *,
        page_size: int = 50,
        page_no: int = 1,
        client_id: int | None = None,
        agent_id: int | None = None,
        search: str | None = None,
        **params: Any,
    ) -> PaginatedResponse[Opportunity]:
        params.update(
            {k: v for k, v in {
                "client_id": client_id,
                "agent_id": agent_id,
                "search": search,
            }.items() if v is not None}
        )
        return await super().alist(page_size=page_size, page_no=page_no, **params)
