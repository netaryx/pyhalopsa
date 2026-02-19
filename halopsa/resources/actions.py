"""Actions resource."""

from __future__ import annotations

from typing import Any

from ..models._base import PaginatedResponse
from ..models.action import Action, ActionList
from ._base import CRUDResource


class ActionsResource(CRUDResource[Action, ActionList, ActionList]):
    _path = "Actions"
    _list_key = "actions"
    _model = Action
    _list_model = ActionList

    def list(
        self,
        *,
        page_size: int = 50,
        page_no: int = 1,
        ticket_id: int | None = None,
        agent_id: int | None = None,
        excludesys: bool | None = None,
        **params: Any,
    ) -> PaginatedResponse[ActionList]:
        params.update(
            {k: v for k, v in {
                "ticket_id": ticket_id,
                "agent_id": agent_id,
                "excludesys": excludesys,
            }.items() if v is not None}
        )
        return super().list(page_size=page_size, page_no=page_no, **params)

    async def alist(
        self,
        *,
        page_size: int = 50,
        page_no: int = 1,
        ticket_id: int | None = None,
        agent_id: int | None = None,
        **params: Any,
    ) -> PaginatedResponse[ActionList]:
        params.update(
            {k: v for k, v in {
                "ticket_id": ticket_id,
                "agent_id": agent_id,
            }.items() if v is not None}
        )
        return await super().alist(page_size=page_size, page_no=page_no, **params)
