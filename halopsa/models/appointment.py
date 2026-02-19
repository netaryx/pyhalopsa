"""Appointment models."""

from __future__ import annotations

from datetime import datetime as dt
from typing import Any

from ._base import HaloModel
from ._common import CustomField


class Appointment(HaloModel):
    """Full appointment detail."""

    id: int | None = None
    start: dt | None = None
    end: dt | None = None
    subject: str | None = None
    description: str | None = None
    allday: bool | None = None
    location: str | None = None
    ticket_id: int | None = None
    agent_id: int | None = None
    agents: list[Any] | None = None
    appointment_type_id: int | None = None
    status: str | None = None
    note: str | None = None
    note_html: str | None = None
    complete_date: dt | None = None
    complete_agent_id: int | None = None
    reminderminutes: int | None = None
    client_id: int | None = None
    site_id: int | None = None
    user_id: int | None = None
    customfields: list[CustomField] | None = None
