"""Clients command with typed filters."""

from __future__ import annotations

from typing import Optional

import typer

from .._app import get_client, handle_api_error, state
from .._output import print_detail, print_json, print_table
from .._resource_cmd import JSON_OPTION, make_resource_app, _model_to_dict, _set_json

LIST_COLUMNS = ["id", "name", "toplevel_name", "website", "phone_number", "email_address", "inactive"]
DETAIL_COLUMNS = [
    "id", "name", "toplevel_id", "toplevel_name", "inactive", "colour",
    "main_site_id", "sla_id", "website", "phone_number", "email_address",
    "notes", "ticket_count", "contract_count",
]

# Start with the factory for get/create/update/delete
app = make_resource_app(
    name="clients",
    resource_attr="clients",
    list_columns=LIST_COLUMNS,
    detail_columns=DETAIL_COLUMNS,
)


# Override list with typed filters
@app.command("list", rich_help_panel="Commands")
def list_cmd(
    page_size: int = typer.Option(50, "--page-size", "-n", help="Results per page."),
    page_no: int = typer.Option(1, "--page", "-p", help="Page number."),
    search: Optional[str] = typer.Option(None, "--search", "-s", help="Search term."),
    toplevel_id: Optional[int] = typer.Option(None, "--toplevel-id", help="Filter by top-level ID."),
    inactive: Optional[bool] = typer.Option(None, "--inactive", help="Filter by inactive status."),
    all_pages: bool = typer.Option(False, "--all", help="Fetch all pages."),
    json_output: bool = JSON_OPTION,
) -> None:
    """List clients with optional filters."""
    _set_json(json_output)
    try:
        client = get_client()
        kwargs = {}
        if search is not None:
            kwargs["search"] = search
        if toplevel_id is not None:
            kwargs["toplevel_id"] = toplevel_id
        if inactive is not None:
            kwargs["inactive"] = inactive

        if all_pages:
            items_raw = list(client.clients.list_all(page_size=page_size, **kwargs))
            items = [_model_to_dict(i) for i in items_raw]
        else:
            result = client.clients.list(page_size=page_size, page_no=page_no, **kwargs)
            items = [_model_to_dict(i) for i in result.items]

        if state.json_output:
            print_json(items)
        else:
            print_table(items, LIST_COLUMNS, title="Clients")
    except SystemExit:
        raise
    except Exception as e:
        handle_api_error(e)
