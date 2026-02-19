"""Projects resource."""

from __future__ import annotations

from typing import Any

from ..models._base import PaginatedResponse
from ..models.project import Project
from ._base import CRUDResource


class ProjectsResource(CRUDResource[Project, Project, Project]):
    _path = "Projects"
    _list_key = "tickets"
    _model = Project
    _list_model = Project

    def list(
        self,
        *,
        page_size: int = 50,
        page_no: int = 1,
        client_id: int | None = None,
        agent_id: int | None = None,
        search: str | None = None,
        open_only: bool | None = None,
        **params: Any,
    ) -> PaginatedResponse[Project]:
        params.update(
            {k: v for k, v in {
                "client_id": client_id,
                "agent_id": agent_id,
                "search": search,
                "open_only": open_only,
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
    ) -> PaginatedResponse[Project]:
        params.update(
            {k: v for k, v in {
                "client_id": client_id,
                "search": search,
            }.items() if v is not None}
        )
        return await super().alist(page_size=page_size, page_no=page_no, **params)
