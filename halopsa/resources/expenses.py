"""Expenses resource."""

from __future__ import annotations

from typing import Any

from ..models._base import PaginatedResponse
from ..models.expense import Expense
from ._base import CRUDResource


class ExpensesResource(CRUDResource[Expense, Expense, Expense]):
    _path = "Expense"
    _list_key = "expenses"
    _model = Expense
    _list_model = Expense

    def _parse_list(self, data: Any) -> PaginatedResponse[Expense]:
        if isinstance(data, list):
            items = [self._list_model.model_validate(i) for i in data]
            return PaginatedResponse[Expense](record_count=len(items), items=items)
        return super()._parse_list(data)

    def list(
        self,
        *,
        page_size: int = 50,
        page_no: int = 1,
        agent_id: int | None = None,
        ticket_id: int | None = None,
        **params: Any,
    ) -> PaginatedResponse[Expense]:
        params.update(
            {k: v for k, v in {
                "agent_id": agent_id,
                "ticket_id": ticket_id,
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
    ) -> PaginatedResponse[Expense]:
        params.update(
            {k: v for k, v in {
                "agent_id": agent_id,
                "ticket_id": ticket_id,
            }.items() if v is not None}
        )
        return await super().alist(page_size=page_size, page_no=page_no, **params)

    def delete(self, id: int, **params: Any) -> None:
        raise NotImplementedError("The Expense endpoint does not support DELETE")

    async def adelete(self, id: int, **params: Any) -> None:
        raise NotImplementedError("The Expense endpoint does not support DELETE")
