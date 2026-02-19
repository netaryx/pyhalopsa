"""Attachments command with typed filters."""

from __future__ import annotations

from typing import Optional

import typer

from .._app import get_client, handle_api_error, state
from .._output import print_detail, print_json, print_table
from .._resource_cmd import JSON_OPTION, make_resource_app, _model_to_dict, _set_json

LIST_COLUMNS = ["id", "filename", "ticket_id", "action_id", "filesize", "datecreated", "isimage"]
DETAIL_COLUMNS = [
    "id", "filename", "datecreated", "note", "filesize", "type", "unique_id",
    "isimage", "ticket_id", "action_id", "user_id", "agent_id",
    "content_type", "link",
]

app = make_resource_app(
    name="attachments",
    resource_attr="attachments",
    list_columns=LIST_COLUMNS,
    detail_columns=DETAIL_COLUMNS,
)


@app.command("list", rich_help_panel="Commands")
def list_cmd(
    page_size: int = typer.Option(50, "--page-size", "-n", help="Results per page."),
    page_no: int = typer.Option(1, "--page", "-p", help="Page number."),
    ticket_id: Optional[int] = typer.Option(None, "--ticket-id", help="Filter by ticket ID."),
    action_id: Optional[int] = typer.Option(None, "--action-id", help="Filter by action ID."),
    all_pages: bool = typer.Option(False, "--all", help="Fetch all pages."),
    json_output: bool = JSON_OPTION,
) -> None:
    """List attachments with optional filters."""
    _set_json(json_output)
    try:
        client = get_client()
        kwargs = {}
        if ticket_id is not None:
            kwargs["ticket_id"] = ticket_id
        if action_id is not None:
            kwargs["action_id"] = action_id

        if all_pages:
            items_raw = list(client.attachments.list_all(page_size=page_size, **kwargs))
            items = [_model_to_dict(i) for i in items_raw]
        else:
            result = client.attachments.list(page_size=page_size, page_no=page_no, **kwargs)
            items = [_model_to_dict(i) for i in result.items]

        if state.json_output:
            print_json(items)
        else:
            print_table(items, LIST_COLUMNS, title="Attachments")
    except SystemExit:
        raise
    except Exception as e:
        handle_api_error(e)
