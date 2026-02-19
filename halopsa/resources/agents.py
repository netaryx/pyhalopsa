"""Agents resource."""

from __future__ import annotations

from typing import Any

from ..models._base import PaginatedResponse
from ..models.agent import Agent, AgentList
from ._base import CRUDResource


class AgentsResource(CRUDResource[Agent, AgentList, AgentList]):
    _path = "Agent"
    _list_key = "agents"
    _model = Agent
    _list_model = AgentList

    def _parse_list(self, data: Any) -> PaginatedResponse[AgentList]:
        # Agent endpoint may return a bare list
        if isinstance(data, list):
            items = [self._list_model.model_validate(i) for i in data]
            return PaginatedResponse[AgentList](record_count=len(items), items=items)
        return super()._parse_list(data)

    def list(
        self,
        *,
        page_size: int = 50,
        page_no: int = 1,
        team_id: int | None = None,
        department_id: int | None = None,
        search: str | None = None,
        includeenabled: bool | None = None,
        includedisabled: bool | None = None,
        **params: Any,
    ) -> PaginatedResponse[AgentList]:
        params.update(
            {k: v for k, v in {
                "team_id": team_id,
                "department_id": department_id,
                "search": search,
                "includeenabled": includeenabled,
                "includedisabled": includedisabled,
            }.items() if v is not None}
        )
        return super().list(page_size=page_size, page_no=page_no, **params)

    async def alist(
        self,
        *,
        page_size: int = 50,
        page_no: int = 1,
        team_id: int | None = None,
        search: str | None = None,
        **params: Any,
    ) -> PaginatedResponse[AgentList]:
        params.update(
            {k: v for k, v in {
                "team_id": team_id,
                "search": search,
            }.items() if v is not None}
        )
        return await super().alist(page_size=page_size, page_no=page_no, **params)

    def me(self) -> Agent:
        """Get the currently authenticated agent."""
        data = self._client.request("GET", "Agent/me")
        return Agent.model_validate(data)

    async def ame(self) -> Agent:
        data = await self._client.arequest("GET", "Agent/me")
        return Agent.model_validate(data)
