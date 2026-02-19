"""Site (ServSite) models."""

from __future__ import annotations

from ._base import HaloModel
from ._common import CustomField


class SiteList(HaloModel):
    """Abbreviated site returned by list endpoints."""

    id: int | None = None
    name: str | None = None
    display_name: str | None = None
    client_id: int | None = None
    client_name: str | None = None
    phonenumber: str | None = None
    inactive: bool | None = None
    main_site: bool | None = None
    colour: str | None = None


class Site(HaloModel):
    """Full site detail."""

    id: int | None = None
    name: str | None = None
    display_name: str | None = None
    summary: str | None = None
    client_id: int | None = None
    client_name: str | None = None
    phonenumber: str | None = None
    address: str | None = None
    colour: str | None = None
    inactive: bool | None = None
    notes: str | None = None
    use: str | None = None
    sla_id: int | None = None
    main_site: bool | None = None
    customfields: list[CustomField] | None = None
