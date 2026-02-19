"""Webhooks resource."""

from __future__ import annotations

from typing import Any

from ..models._base import PaginatedResponse
from ..models.webhook import Webhook
from ._base import CRUDResource


class WebhooksResource(CRUDResource[Webhook, Webhook, Webhook]):
    _path = "Webhook"
    _list_key = "webhooks"
    _model = Webhook
    _list_model = Webhook

    def _parse_list(self, data: Any) -> PaginatedResponse[Webhook]:
        if isinstance(data, list):
            items = [self._list_model.model_validate(i) for i in data]
            return PaginatedResponse[Webhook](record_count=len(items), items=items)
        return super()._parse_list(data)
