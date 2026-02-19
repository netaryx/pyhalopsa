"""Timesheet model."""

from __future__ import annotations

from typing import Any

from ._base import HaloModel


class Timesheet(HaloModel):
    id: int | None = None
    agent_id: int | None = None
    agent_name: str | None = None
    colour: str | None = None
    date: str | None = None
    start_time: str | None = None
    end_time: str | None = None
    estimated_start_time: str | None = None
    estimated_end_time: str | None = None
    target_hours: float | None = None
    actual_hours: float | None = None
    break_hours: float | None = None
    unlogged_hours: float | None = None
    allowed_break_hours: float | None = None
    work_hours: float | None = None
    percentage: float | None = None
    workdayid: int | None = None
    events: list[Any] | None = None
    chargeable_hours: float | None = None
    forecasting_hours: float | None = None
    approval: Any | None = None
