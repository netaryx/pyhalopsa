"""Sites resource."""

from __future__ import annotations

from typing import Any

from ..models._base import PaginatedResponse
from ..models.site import Site, SiteList
from ._base import CRUDResource


class SitesResource(CRUDResource[Site, SiteList, SiteList]):
    _path = "Site"
    _list_key = "sites"
    _model = Site
    _list_model = SiteList

    def list(
        self,
        *,
        page_size: int = 50,
        page_no: int = 1,
        client_id: int | None = None,
        search: str | None = None,
        **params: Any,
    ) -> PaginatedResponse[SiteList]:
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
    ) -> PaginatedResponse[SiteList]:
        params.update(
            {k: v for k, v in {
                "client_id": client_id,
                "search": search,
            }.items() if v is not None}
        )
        return await super().alist(page_size=page_size, page_no=page_no, **params)
