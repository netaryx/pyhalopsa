"""Users command with typed filters and 'me' subcommand."""

from __future__ import annotations

from typing import Optional

import typer

from .._app import get_client, handle_api_error, state
from .._output import print_detail, print_json, print_table
from .._resource_cmd import JSON_OPTION, make_resource_app, _model_to_dict, _set_json

LIST_COLUMNS = ["id", "name", "emailaddress", "client_name", "site_name", "inactive"]
DETAIL_COLUMNS = [
    "id", "name", "firstname", "surname", "emailaddress",
    "phonenumber", "mobilenumber", "client_id", "client_name",
    "site_id", "site_name", "inactive", "isimportantcontact", "login",
]

app = make_resource_app(
    name="users",
    resource_attr="users",
    list_columns=LIST_COLUMNS,
    detail_columns=DETAIL_COLUMNS,
)


@app.command("list", rich_help_panel="Commands")
def list_cmd(
    page_size: int = typer.Option(50, "--page-size", "-n", help="Results per page."),
    page_no: int = typer.Option(1, "--page", "-p", help="Page number."),
    client_id: Optional[int] = typer.Option(None, "--client-id", help="Filter by client ID."),
    site_id: Optional[int] = typer.Option(None, "--site-id", help="Filter by site ID."),
    search: Optional[str] = typer.Option(None, "--search", "-s", help="Search term."),
    inactive: Optional[bool] = typer.Option(None, "--inactive", help="Filter by inactive status."),
    all_pages: bool = typer.Option(False, "--all", help="Fetch all pages."),
    json_output: bool = JSON_OPTION,
) -> None:
    """List users with optional filters."""
    _set_json(json_output)
    try:
        client = get_client()
        kwargs = {}
        if client_id is not None:
            kwargs["client_id"] = client_id
        if site_id is not None:
            kwargs["site_id"] = site_id
        if search is not None:
            kwargs["search"] = search
        if inactive is not None:
            kwargs["inactive"] = inactive

        if all_pages:
            items_raw = list(client.users.list_all(page_size=page_size, **kwargs))
            items = [_model_to_dict(i) for i in items_raw]
        else:
            result = client.users.list(page_size=page_size, page_no=page_no, **kwargs)
            items = [_model_to_dict(i) for i in result.items]

        if state.json_output:
            print_json(items)
        else:
            print_table(items, LIST_COLUMNS, title="Users")
    except SystemExit:
        raise
    except Exception as e:
        handle_api_error(e)


@app.command("me")
def me_cmd(
    json_output: bool = JSON_OPTION,
) -> None:
    """Get the currently authenticated user."""
    _set_json(json_output)
    try:
        client = get_client()
        item = client.users.me()
        data = _model_to_dict(item)
        if state.json_output:
            print_json(data)
        else:
            print_detail(data, DETAIL_COLUMNS)
    except SystemExit:
        raise
    except Exception as e:
        handle_api_error(e)
