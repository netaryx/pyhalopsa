"""Status model."""

from __future__ import annotations

from ._base import HaloModel


class Status(HaloModel):
    id: int | None = None
    name: str | None = None
    type: str | None = None
    colour: str | None = None
    treatasopen: bool | None = None
    treatasclose: bool | None = None
    treatasonhold: bool | None = None
    sequence: int | None = None
    use: str | None = None
    note: str | None = None
