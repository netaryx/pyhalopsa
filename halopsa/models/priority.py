"""Priority model."""

from __future__ import annotations

from ._base import HaloModel


class Priority(HaloModel):
    id: int | None = None
    name: str | None = None
    colour: str | None = None
    sequence: int | None = None
    ishidden: bool | None = None
    severity: str | None = None
    noaliases: bool | None = None
    use: str | None = None
