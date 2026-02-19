"""User (end-user / contact) models."""

from __future__ import annotations

from ._base import HaloModel
from ._common import CustomField


class UserList(HaloModel):
    """Abbreviated user returned by list endpoints."""

    id: int | None = None
    name: str | None = None
    firstname: str | None = None
    surname: str | None = None
    initials: str | None = None
    emailaddress: str | None = None
    client_id: int | None = None
    client_name: str | None = None
    site_id: int | None = None
    site_name: str | None = None
    inactive: bool | None = None
    isimportantcontact: bool | None = None
    phonenumber: str | None = None
    mobilenumber: str | None = None


class User(HaloModel):
    """Full user / contact detail."""

    id: int | None = None
    name: str | None = None
    firstname: str | None = None
    surname: str | None = None
    initials: str | None = None
    title: str | None = None
    emailaddress: str | None = None
    email2: str | None = None
    email3: str | None = None
    phonenumber: str | None = None
    mobilenumber: str | None = None
    homenumber: str | None = None
    fax: str | None = None
    telpref: int | None = None
    inactive: bool | None = None
    isimportantcontact: bool | None = None
    client_id: int | None = None
    client_name: str | None = None
    site_id: int | None = None
    site_name: str | None = None
    notes: str | None = None
    login: str | None = None
    isserviceaccount: bool | None = None
    linked_agent_id: int | None = None
    never_send_emails: bool | None = None
    customfields: list[CustomField] | None = None
