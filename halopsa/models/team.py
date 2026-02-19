"""Team model."""

from __future__ import annotations

from ._base import HaloModel


class Team(HaloModel):
    id: int | None = None
    name: str | None = None
    department_id: int | None = None
    department_name: str | None = None
    ticket_count: int | None = None
    sequence: int | None = None
    description: str | None = None
    inactive: bool | None = None
    use: str | None = None
    colour: str | None = None
