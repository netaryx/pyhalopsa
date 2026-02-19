"""Attachment models."""

from __future__ import annotations

from datetime import datetime as dt
from typing import Any

from ._base import HaloModel


class Attachment(HaloModel):
    """Full attachment detail."""

    id: int | None = None
    filename: str | None = None
    datecreated: dt | None = None
    note: str | None = None
    filesize: int | None = None
    type: str | None = None
    unique_id: str | None = None
    isimage: bool | None = None
    ticket_id: int | None = None
    action_id: int | None = None
    user_id: int | None = None
    agent_id: int | None = None
    content_type: str | None = None
    data: Any | None = None
    link: str | None = None
