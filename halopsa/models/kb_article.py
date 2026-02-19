"""Knowledge-base article models."""

from __future__ import annotations

from datetime import datetime as dt

from ._base import HaloModel
from ._common import CustomField


class KBArticleList(HaloModel):
    """Abbreviated KB article returned by list endpoints."""

    id: int | None = None
    name: str | None = None
    view_count: int | None = None
    useful_count: int | None = None
    notuseful_count: int | None = None
    date_created: dt | None = None
    date_edited: dt | None = None
    tag_string: str | None = None
    inactive: bool | None = None
    type: str | None = None


class KBArticle(HaloModel):
    """Full KB article detail returned by single-get endpoints."""

    id: int | None = None
    name: str | None = None
    description: str | None = None
    view_count: int | None = None
    useful_count: int | None = None
    notuseful_count: int | None = None
    date_created: dt | None = None
    date_edited: dt | None = None
    tag_string: str | None = None
    inactive: bool | None = None
    type: str | None = None
    next_review_date: dt | None = None
    customfields: list[CustomField] | None = None
    editor_type: str | None = None
    creator_id: int | None = None
    creator_name: str | None = None
    editor_id: int | None = None
    editor_name: str | None = None
    resolution: str | None = None
    link: str | None = None
