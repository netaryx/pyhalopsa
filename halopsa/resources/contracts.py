"""Contracts resource."""

from __future__ import annotations

from typing import Any

from ..models._base import PaginatedResponse
from ..models.contract import Contract, ContractList
from ._base import CRUDResource


class ContractsResource(CRUDResource[Contract, ContractList, ContractList]):
    _path = "ClientContract"
    _list_key = "contracts"
    _model = Contract
    _list_model = ContractList

    def list(
        self,
        *,
        page_size: int = 50,
        page_no: int = 1,
        client_id: int | None = None,
        search: str | None = None,
        **params: Any,
    ) -> PaginatedResponse[ContractList]:
        params.update(
            {k: v for k, v in {
                "client_id": client_id,
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
        search: str | None = None,
        **params: Any,
    ) -> PaginatedResponse[ContractList]:
        params.update(
            {k: v for k, v in {
                "client_id": client_id,
                "search": search,
            }.items() if v is not None}
        )
        return await super().alist(page_size=page_size, page_no=page_no, **params)
