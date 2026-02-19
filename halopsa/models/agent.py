"""Agent models."""

from __future__ import annotations

from ._base import HaloModel
from ._common import CustomField


class AgentList(HaloModel):
    """Abbreviated agent returned by list endpoints."""

    id: int | None = None
    name: str | None = None
    email: str | None = None
    team_id: int | None = None
    team: str | None = None
    role: str | None = None
    isadmin: bool | None = None
    is_disabled: bool | None = None
    initials: str | None = None
    colour: str | None = None
    jobtitle: str | None = None


class Agent(HaloModel):
    """Full agent detail."""

    id: int | None = None
    name: str | None = None
    email: str | None = None
    team_id: int | None = None
    team: str | None = None
    role: str | None = None
    isadmin: bool | None = None
    is_disabled: bool | None = None
    initials: str | None = None
    colour: str | None = None
    department_id: int | None = None
    cab_id: int | None = None
    cab_name: str | None = None
    override_sla: bool | None = None
    phonenumber: str | None = None
    mobilenumber: str | None = None
    jobtitle: str | None = None
    login: str | None = None
    use: str | None = None
    customfields: list[CustomField] | None = None
