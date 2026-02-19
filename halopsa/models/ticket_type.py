"""TicketType model."""

from __future__ import annotations

from ._base import HaloModel


class TicketType(HaloModel):
    id: int | None = None
    name: str | None = None
    use: str | None = None
    sequence: int | None = None
    colour: str | None = None
    inactive: bool | None = None
    default_team_id: int | None = None
    default_agent_id: int | None = None
    default_sla_id: int | None = None
    default_priority_id: int | None = None
    prefix: str | None = None
    autoincrement: bool | None = None
    showinusercatalog: bool | None = None
    showintechcatalog: bool | None = None
