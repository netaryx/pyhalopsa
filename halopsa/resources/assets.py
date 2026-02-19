"""Assets resource."""

from __future__ import annotations

from typing import Any

from ..models._base import PaginatedResponse
from ..models.asset import Asset, AssetList
from ._base import CRUDResource


class AssetsResource(CRUDResource[Asset, AssetList, AssetList]):
    _path = "Asset"
    _list_key = "assets"
    _model = Asset
    _list_model = AssetList

    def list(
        self,
        *,
        page_size: int = 50,
        page_no: int = 1,
        client_id: int | None = None,
        site_id: int | None = None,
        assettype_id: int | None = None,
        search: str | None = None,
        contract_id: int | None = None,
        ticket_id: int | None = None,
        **params: Any,
    ) -> PaginatedResponse[AssetList]:
        params.update(
            {k: v for k, v in {
                "client_id": client_id,
                "site_id": site_id,
                "assettype_id": assettype_id,
                "search": search,
                "contract_id": contract_id,
                "ticket_id": ticket_id,
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
        search: str | None = None,
        **params: Any,
    ) -> PaginatedResponse[AssetList]:
        params.update(
            {k: v for k, v in {
                "client_id": client_id,
                "site_id": site_id,
                "search": search,
            }.items() if v is not None}
        )
        return await super().alist(page_size=page_size, page_no=page_no, **params)
