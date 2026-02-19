"""Webhook model."""

from __future__ import annotations

from typing import Any

from ._base import HaloModel


class Webhook(HaloModel):
    id: int | None = None
    name: str | None = None
    type: str | None = None
    url: str | None = None
    content_type: str | None = None
    authentication_type: str | None = None
    method: str | None = None
    basic_username: str | None = None
    basic_password: str | None = None
    certificate_id: int | None = None
    certificate_name: str | None = None
    active: bool | None = None
    events: list[Any] | None = None
    last_status: str | None = None
    systemuse: bool | None = None
    inbound_authentication_type: str | None = None
    authentication_header: str | None = None
    headers_to_sign: str | None = None
