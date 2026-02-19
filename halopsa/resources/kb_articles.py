"""KB Articles resource."""

from __future__ import annotations

from typing import Any

from ..models._base import PaginatedResponse
from ..models.kb_article import KBArticle, KBArticleList
from ._base import CRUDResource


class KBArticlesResource(CRUDResource[KBArticle, KBArticleList, KBArticleList]):
    _path = "KBArticle"
    _list_key = "articles"
    _model = KBArticle
    _list_model = KBArticleList

    def list(
        self,
        *,
        page_size: int = 50,
        page_no: int = 1,
        search: str | None = None,
        type: int | None = None,
        inactive: bool | None = None,
        **params: Any,
    ) -> PaginatedResponse[KBArticleList]:
        params.update(
            {k: v for k, v in {
                "search": search,
                "type": type,
                "inactive": inactive,
            }.items() if v is not None}
        )
        return super().list(page_size=page_size, page_no=page_no, **params)

    async def alist(
        self,
        *,
        page_size: int = 50,
        page_no: int = 1,
        search: str | None = None,
        **params: Any,
    ) -> PaginatedResponse[KBArticleList]:
        params.update(
            {k: v for k, v in {
                "search": search,
            }.items() if v is not None}
        )
        return await super().alist(page_size=page_size, page_no=page_no, **params)
