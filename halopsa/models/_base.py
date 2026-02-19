"""Base model and paginated response."""

from __future__ import annotations

from typing import Generic, TypeVar

from pydantic import BaseModel, ConfigDict

T = TypeVar("T")


class HaloModel(BaseModel):
    """Base for all HaloPSA models.

    ``extra="allow"`` captures the hundreds of undocumented fields the API
    returns without breaking validation.
    """

    model_config = ConfigDict(extra="allow", populate_by_name=True)


class PaginatedResponse(BaseModel, Generic[T]):
    """Wrapper returned by every list endpoint."""

    model_config = ConfigDict(extra="allow")

    record_count: int = 0
    items: list[T] = []
    page_no: int = 1
    page_size: int = 50

    @property
    def has_next(self) -> bool:
        return self.page_no * self.page_size < self.record_count
