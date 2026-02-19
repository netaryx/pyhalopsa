"""Software Licences resource."""

from __future__ import annotations

from typing import Any

from ..models._base import PaginatedResponse
from ..models.software_licence import SoftwareLicence
from ._base import CRUDResource


class SoftwareLicencesResource(CRUDResource[SoftwareLicence, SoftwareLicence, SoftwareLicence]):
    _path = "SoftwareLicence"
    _list_key = "softwarelicences"
    _model = SoftwareLicence
    _list_model = SoftwareLicence

    def _parse_list(self, data: Any) -> PaginatedResponse[SoftwareLicence]:
        if isinstance(data, list):
            items = [self._list_model.model_validate(i) for i in data]
            return PaginatedResponse[SoftwareLicence](record_count=len(items), items=items)
        return super()._parse_list(data)

    def list(
        self,
        *,
        page_size: int = 50,
        page_no: int = 1,
        client_id: int | None = None,
        search: str | None = None,
        **params: Any,
    ) -> PaginatedResponse[SoftwareLicence]:
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
    ) -> PaginatedResponse[SoftwareLicence]:
        params.update(
            {k: v for k, v in {
                "client_id": client_id,
                "search": search,
            }.items() if v is not None}
        )
        return await super().alist(page_size=page_size, page_no=page_no, **params)
