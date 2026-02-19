"""Report model."""

from __future__ import annotations

from typing import Any

from ._base import HaloModel


class Report(HaloModel):
    id: int | None = None
    name: str | None = None
    sql: str | None = None
    reportingperiod: str | None = None
    reportingperiodstartdate: str | None = None
    reportingperiodenddate: str | None = None
    charttitle: str | None = None
    charttype: str | None = None
    xaxis: str | None = None
    yaxis: str | None = None
    count: bool | None = None
    sum: bool | None = None
    average: bool | None = None
    availablefields: list[Any] | None = None
    selectedfields: list[Any] | None = None
    use: str | None = None
