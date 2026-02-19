"""Shared types used across multiple models."""

from __future__ import annotations

from typing import Any

from pydantic import Field

from ._base import HaloModel


class CustomField(HaloModel):
    """A custom field value attached to many HaloPSA entities."""

    id: int | None = None
    name: str | None = None
    value: Any | None = None
    type: int | None = None
    display: str | None = None
    label: str | None = None


class CFValue(HaloModel):
    """Convenience alias used in some endpoints."""

    id: int | None = None
    value: Any | None = None


class Colour(HaloModel):
    """Colour info returned on several lookup entities."""

    id: int | None = None
    name: str | None = None
    colour: str | None = Field(default=None, alias="colour")
