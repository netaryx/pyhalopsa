"""SLA model."""

from __future__ import annotations

from typing import Any

from ._base import HaloModel


class SLA(HaloModel):
    id: int | None = None
    name: str | None = None
    workday_id: int | None = None
    responsereset: bool | None = None
    autoreleaseoption: int | None = None
    workdays: list[Any] | None = None
    rules: list[Any] | None = None
    use: str | None = None
