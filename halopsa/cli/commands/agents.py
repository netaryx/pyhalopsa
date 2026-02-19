"""Agents command with typed filters and 'me' subcommand."""

from __future__ import annotations

from typing import Optional

import typer

from .._app import get_client, handle_api_error, state
from .._output import print_detail, print_json, print_table
from .._resource_cmd import JSON_OPTION, make_resource_app, _model_to_dict, _set_json

LIST_COLUMNS = ["id", "name", "email", "team", "role", "is_disabled"]
DETAIL_COLUMNS = [
    "id", "name", "email", "team_id", "team", "role", "isadmin", "is_disabled",
    "initials", "colour", "jobtitle", "phonenumber", "mobilenumber", "login",
]

app = make_resource_app(
    name="agents",
    resource_attr="agents",
    list_columns=LIST_COLUMNS,
    detail_columns=DETAIL_COLUMNS,
)


@app.command("list", rich_help_panel="Commands")
def list_cmd(
    page_size: int = typer.Option(50, "--page-size", "-n", help="Results per page."),
    page_no: int = typer.Option(1, "--page", "-p", help="Page number."),
    team_id: Optional[int] = typer.Option(None, "--team-id", help="Filter by team ID."),
    department_id: Optional[int] = typer.Option(None, "--department-id", help="Filter by department ID."),
    search: Optional[str] = typer.Option(None, "--search", "-s", help="Search term."),
    include_disabled: Optional[bool] = typer.Option(None, "--include-disabled", help="Include disabled agents."),
    all_pages: bool = typer.Option(False, "--all", help="Fetch all pages."),
    json_output: bool = JSON_OPTION,
) -> None:
    """List agents with optional filters."""
    _set_json(json_output)
    try:
        client = get_client()
        kwargs = {}
        if team_id is not None:
            kwargs["team_id"] = team_id
        if department_id is not None:
            kwargs["department_id"] = department_id
        if search is not None:
            kwargs["search"] = search
        if include_disabled:
            kwargs["includedisabled"] = True

        if all_pages:
            items_raw = list(client.agents.list_all(page_size=page_size, **kwargs))
            items = [_model_to_dict(i) for i in items_raw]
        else:
            result = client.agents.list(page_size=page_size, page_no=page_no, **kwargs)
            items = [_model_to_dict(i) for i in result.items]

        if state.json_output:
            print_json(items)
        else:
            print_table(items, LIST_COLUMNS, title="Agents")
    except SystemExit:
        raise
    except Exception as e:
        handle_api_error(e)


@app.command("me")
def me_cmd(
    json_output: bool = JSON_OPTION,
) -> None:
    """Get the currently authenticated agent."""
    _set_json(json_output)
    try:
        client = get_client()
        item = client.agents.me()
        data = _model_to_dict(item)
        if state.json_output:
            print_json(data)
        else:
            print_detail(data, DETAIL_COLUMNS)
    except SystemExit:
        raise
    except Exception as e:
        handle_api_error(e)
