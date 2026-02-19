"""Category model."""

from __future__ import annotations

from ._base import HaloModel


class Category(HaloModel):
    id: int | None = None
    value: str | None = None
    category_name: str | None = None
    type_id: int | None = None
    sla_id: int | None = None
    priority_id: int | None = None
    chargerate: float | None = None
    category_group_id: int | None = None
    sequence: int | None = None
    inactive: bool | None = None
    use: str | None = None
