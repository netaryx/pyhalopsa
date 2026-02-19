"""Action (ticket-action / note) models."""

from __future__ import annotations

from datetime import datetime as dt

from ._base import HaloModel
from ._common import CustomField


class ActionList(HaloModel):
    """Abbreviated action returned by list endpoints."""

    id: int | None = None
    ticket_id: int | None = None
    outcome: str | None = None
    outcome_id: int | None = None
    who: str | None = None
    who_agentid: int | None = None
    who_type: int | None = None
    datetime: dt | None = None
    last_updated: dt | None = None
    note: str | None = None
    hiddenfromuser: bool | None = None
    timetaken: float | None = None
    important: bool | None = None
    new_status: int | None = None


class Action(HaloModel):
    """Full action detail returned by single-get endpoints."""

    id: int | None = None
    ticket_id: int | None = None
    outcome: str | None = None
    outcome_id: int | None = None
    who: str | None = None
    who_agentid: int | None = None
    who_type: int | None = None
    datetime: dt | None = None
    last_updated: dt | None = None
    note: str | None = None
    note_html: str | None = None
    emailfrom: str | None = None
    emailto: str | None = None
    emailcc: str | None = None
    hiddenfromuser: bool | None = None
    timetaken: float | None = None
    actionarrivaldate: dt | None = None
    actioncompletiondate: dt | None = None
    important: bool | None = None
    new_status: int | None = None
    sendemail: bool | None = None
    sla_hold: bool | None = None
    attachment_list: list | None = None
    customfields: list[CustomField] | None = None
