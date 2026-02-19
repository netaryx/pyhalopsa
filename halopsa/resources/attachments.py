"""Attachments resource with S3 presigned URL upload flow."""

from __future__ import annotations

from typing import Any

from ..models._base import PaginatedResponse
from ..models.attachment import Attachment
from ._base import CRUDResource


class AttachmentsResource(CRUDResource[Attachment, Attachment, Attachment]):
    _path = "Attachment"
    _list_key = "attachments"
    _model = Attachment
    _list_model = Attachment

    def list(
        self,
        *,
        page_size: int = 50,
        page_no: int = 1,
        ticket_id: int | None = None,
        action_id: int | None = None,
        type: int | None = None,
        **params: Any,
    ) -> PaginatedResponse[Attachment]:
        params.update(
            {k: v for k, v in {
                "ticket_id": ticket_id,
                "action_id": action_id,
                "type": type,
            }.items() if v is not None}
        )
        return super().list(page_size=page_size, page_no=page_no, **params)

    async def alist(
        self,
        *,
        page_size: int = 50,
        page_no: int = 1,
        ticket_id: int | None = None,
        action_id: int | None = None,
        **params: Any,
    ) -> PaginatedResponse[Attachment]:
        params.update(
            {k: v for k, v in {
                "ticket_id": ticket_id,
                "action_id": action_id,
            }.items() if v is not None}
        )
        return await super().alist(page_size=page_size, page_no=page_no, **params)

    # ── S3 presigned URL upload flow ─────────────────────────────────

    def get_upload_url(self, filename: str) -> dict[str, Any]:
        """Get an S3 presigned URL for uploading a file.

        Returns a dict with ``url`` and ``fields`` for the upload.
        """
        data = self._client.request(
            "POST",
            "Attachment/GetS3PresignedURL",
            json_body={"filename": filename},
        )
        return data

    async def aget_upload_url(self, filename: str) -> dict[str, Any]:
        data = await self._client.arequest(
            "POST",
            "Attachment/GetS3PresignedURL",
            json_body={"filename": filename},
        )
        return data

    def complete_upload(self, **kwargs: Any) -> Attachment:
        """Notify HaloPSA that an S3 upload is complete."""
        data = self._client.request(
            "POST",
            "Attachment/PresignedURLUploadComplete",
            json_body=kwargs,
        )
        if isinstance(data, list) and data:
            return Attachment.model_validate(data[0])
        return Attachment.model_validate(data)

    async def acomplete_upload(self, **kwargs: Any) -> Attachment:
        data = await self._client.arequest(
            "POST",
            "Attachment/PresignedURLUploadComplete",
            json_body=kwargs,
        )
        if isinstance(data, list) and data:
            return Attachment.model_validate(data[0])
        return Attachment.model_validate(data)
