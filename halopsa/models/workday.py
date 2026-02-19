"""Workday model."""

from __future__ import annotations

from typing import Any

from ._base import HaloModel


class Workday(HaloModel):
    id: int | None = None
    name: str | None = None
    summary: str | None = None
    timezone: str | None = None
    start: str | None = None
    end: str | None = None
    incmonday: bool | None = None
    inctuesday: bool | None = None
    incwednesday: bool | None = None
    incthursday: bool | None = None
    incfriday: bool | None = None
    incsaturday: bool | None = None
    incsunday: bool | None = None
    breaks: list[Any] | None = None
    holidays: list[Any] | None = None
