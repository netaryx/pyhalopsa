"""Project models.

Projects use the same Faults_View / "tickets" key as Tickets,
with additional project-management fields.
"""

from __future__ import annotations

from datetime import datetime as dt

from ._base import HaloModel
from ._common import CustomField


class Project(HaloModel):
    """Full project detail returned by single-get endpoints."""

    # -- Core ticket fields (Faults_View) --
    id: int | None = None
    summary: str | None = None
    details: str | None = None
    details_html: str | None = None
    dateoccurred: dt | None = None
    status_id: int | None = None
    status_name: str | None = None
    tickettype_id: int | None = None
    tickettype_name: str | None = None
    priority_id: int | None = None
    sla_id: int | None = None
    sla_name: str | None = None
    client_id: int | None = None
    client_name: str | None = None
    site_id: int | None = None
    site_name: str | None = None
    user_id: int | None = None
    user_name: str | None = None
    team_id: int | None = None
    team: str | None = None
    agent_id: int | None = None
    agent_name: str | None = None
    category_1: str | None = None
    category_2: str | None = None
    category_3: str | None = None
    category_4: str | None = None
    categoryid_1: int | None = None
    categoryid_2: int | None = None
    categoryid_3: int | None = None
    categoryid_4: int | None = None
    impact: str | None = None
    urgency: str | None = None
    estimate: float | None = None
    timetaken: float | None = None
    parent_id: int | None = None
    child_count: int | None = None
    attachment_count: int | None = None
    flagged: bool | None = None
    onhold: bool | None = None
    respondbydate: dt | None = None
    fixbydate: dt | None = None
    deadlinedate: dt | None = None
    dateclosed: dt | None = None
    dateassigned: dt | None = None
    lastactiondate: dt | None = None
    last_update: dt | None = None
    tags: list[str] | None = None
    opportunityid: int | None = None
    customfields: list[CustomField] | None = None

    # -- Project-specific fields --
    projecttimepercentage: float | None = None
    projectcompletionpercentage: float | None = None
    projectearlieststart: dt | None = None
    projectlatestend: dt | None = None
    budget: float | None = None
    budgettype: str | None = None
