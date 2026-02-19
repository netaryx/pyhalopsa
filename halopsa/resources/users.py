"""Users resource."""

from __future__ import annotations

from typing import Any

from ..models._base import PaginatedResponse
from ..models.user import User, UserList
from ._base import CRUDResource


class UsersResource(CRUDResource[User, UserList, UserList]):
    _path = "Users"
    _list_key = "users"
    _model = User
    _list_model = UserList

    def list(
        self,
        *,
        page_size: int = 50,
        page_no: int = 1,
        client_id: int | None = None,
        site_id: int | None = None,
        search: str | None = None,
        inactive: bool | None = None,
        **params: Any,
    ) -> PaginatedResponse[UserList]:
        params.update(
            {k: v for k, v in {
                "client_id": client_id,
                "site_id": site_id,
                "search": search,
                "inactive": inactive,
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
    ) -> PaginatedResponse[UserList]:
        params.update(
            {k: v for k, v in {
                "client_id": client_id,
                "site_id": site_id,
                "search": search,
            }.items() if v is not None}
        )
        return await super().alist(page_size=page_size, page_no=page_no, **params)

    def me(self) -> User:
        """Get the currently authenticated user."""
        data = self._client.request("GET", "Users/me")
        return User.model_validate(data)

    async def ame(self) -> User:
        data = await self._client.arequest("GET", "Users/me")
        return User.model_validate(data)
