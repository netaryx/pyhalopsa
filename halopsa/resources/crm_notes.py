"""CRM Notes resource."""

from __future__ import annotations

from typing import Any

from ..models._base import PaginatedResponse
from ..models.crm_note import CRMNote
from ._base import CRUDResource


class CRMNotesResource(CRUDResource[CRMNote, CRMNote, CRMNote]):
    _path = "CRMNote"
    _list_key = "crmnotes"
    _model = CRMNote
    _list_model = CRMNote

    def _parse_list(self, data: Any) -> PaginatedResponse[CRMNote]:
        if isinstance(data, list):
            items = [self._list_model.model_validate(i) for i in data]
            return PaginatedResponse[CRMNote](record_count=len(items), items=items)
        return super()._parse_list(data)

    def list(
        self,
        *,
        page_size: int = 50,
        page_no: int = 1,
        client_id: int | None = None,
        opportunity_id: int | None = None,
        **params: Any,
    ) -> PaginatedResponse[CRMNote]:
        params.update(
            {k: v for k, v in {
                "client_id": client_id,
                "opportunity_id": opportunity_id,
            }.items() if v is not None}
        )
        return super().list(page_size=page_size, page_no=page_no, **params)

    async def alist(
        self,
        *,
        page_size: int = 50,
        page_no: int = 1,
        client_id: int | None = None,
        **params: Any,
    ) -> PaginatedResponse[CRMNote]:
        params.update(
            {k: v for k, v in {
                "client_id": client_id,
            }.items() if v is not None}
        )
        return await super().alist(page_size=page_size, page_no=page_no, **params)
