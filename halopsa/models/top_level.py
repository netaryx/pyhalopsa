"""TopLevel model."""

from __future__ import annotations

from ._base import HaloModel


class TopLevel(HaloModel):
    id: int | None = None
    name: str | None = None
    inactive: bool | None = None
    sequence: int | None = None
    use: str | None = None
    colour: str | None = None
    note: str | None = None
