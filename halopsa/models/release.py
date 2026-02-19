"""Release model."""

from __future__ import annotations

from ._base import HaloModel


class Release(HaloModel):
    id: int | None = None
    name: str | None = None
    name_expanded: str | None = None
    releasetype_id: int | None = None
    releasetype_name: str | None = None
    branch_id: int | None = None
    branch_name: str | None = None
    whoreleased_id: int | None = None
    builddate: str | None = None
    targetdate: str | None = None
    releasedate: str | None = None
    note: str | None = None
    public_note: str | None = None
    product_id: int | None = None
    product_name: str | None = None
    product_icon: str | None = None
    sequence: int | None = None
    major_version_number: int | None = None
    minor_version_number: int | None = None
    patch_version_number: int | None = None
    releasenote_count: int | None = None
