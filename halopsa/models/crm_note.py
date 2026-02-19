"""CRMNote model."""

from __future__ import annotations

from ._base import HaloModel


class CRMNote(HaloModel):
    id: int | None = None
    client_id: int | None = None
    client_name: str | None = None
    agent_id: int | None = None
    agent_name: str | None = None
    note: str | None = None
    note_html: str | None = None
    datetime: str | None = None
    type: int | None = None
    pinned: bool | None = None
    opportunity_id: int | None = None
