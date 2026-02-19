"""Tickets command with typed filters."""

from __future__ import annotations

import json
from typing import Any, Optional

import typer

from .._app import get_client, handle_api_error, state
from .._output import print_detail, print_json, print_table
from .._resource_cmd import JSON_OPTION, _model_to_dict, _set_json

LIST_COLUMNS = ["id", "summary", "status_name", "client_name", "agent_name", "priority_id", "lastactiondate"]
DETAIL_COLUMNS = [
    "id", "summary", "details", "status_id", "status_name",
    "tickettype_id", "tickettype_name", "priority_id",
    "client_id", "client_name", "site_id", "site_name",
    "user_id", "user_name", "agent_id", "agent_name",
    "team_id", "team", "sla_id", "sla_name",
    "category_1", "category_2", "category_3", "category_4",
    "dateoccurred", "dateclosed", "lastactiondate", "last_update",
    "respondbydate", "fixbydate",
    "flagged", "onhold", "tags",
]

app = typer.Typer(name="tickets", help="Manage tickets.", no_args_is_help=True)


@app.command("list")
def list_cmd(
    page_size: int = typer.Option(50, "--page-size", "-n", help="Results per page."),
    page_no: int = typer.Option(1, "--page", "-p", help="Page number."),
    client_id: Optional[int] = typer.Option(None, "--client-id", help="Filter by client ID."),
    site_id: Optional[int] = typer.Option(None, "--site-id", help="Filter by site ID."),
    user_id: Optional[int] = typer.Option(None, "--user-id", help="Filter by user ID."),
    agent_id: Optional[int] = typer.Option(None, "--agent-id", help="Filter by agent ID."),
    team_id: Optional[int] = typer.Option(None, "--team-id", help="Filter by team ID."),
    status_id: Optional[int] = typer.Option(None, "--status-id", help="Filter by status ID."),
    tickettype_id: Optional[int] = typer.Option(None, "--tickettype-id", help="Filter by ticket type ID."),
    priority_id: Optional[int] = typer.Option(None, "--priority-id", help="Filter by priority ID."),
    sla_id: Optional[int] = typer.Option(None, "--sla-id", help="Filter by SLA ID."),
    open_only: Optional[bool] = typer.Option(None, "--open-only", help="Only open tickets."),
    closed_only: Optional[bool] = typer.Option(None, "--closed-only", help="Only closed tickets."),
    search: Optional[str] = typer.Option(None, "--search", "-s", help="Search term."),
    order: Optional[str] = typer.Option(None, "--order", help="Order by field."),
    order_desc: Optional[bool] = typer.Option(None, "--order-desc", help="Descending order."),
    asset_id: Optional[int] = typer.Option(None, "--asset-id", help="Filter by asset ID."),
    contract_id: Optional[int] = typer.Option(None, "--contract-id", help="Filter by contract ID."),
    all_pages: bool = typer.Option(False, "--all", help="Fetch all pages."),
    json_output: bool = JSON_OPTION,
) -> None:
    """List tickets with optional filters."""
    _set_json(json_output)
    try:
        client = get_client()
        kwargs: dict[str, Any] = {}
        for key, val in {
            "client_id": client_id, "site_id": site_id, "user_id": user_id,
            "agent_id": agent_id, "team_id": team_id, "status_id": status_id,
            "tickettype_id": tickettype_id, "priority_id": priority_id,
            "sla_id": sla_id, "open_only": open_only, "closedonly": closed_only,
            "search": search, "order": order, "orderdesc": order_desc,
            "asset_id": asset_id, "contract_id": contract_id,
        }.items():
            if val is not None:
                kwargs[key] = val

        if all_pages:
            items_raw = list(client.tickets.list_all(page_size=page_size, **kwargs))
            items = [_model_to_dict(i) for i in items_raw]
        else:
            result = client.tickets.list(page_size=page_size, page_no=page_no, **kwargs)
            items = [_model_to_dict(i) for i in result.items]

        if state.json_output:
            print_json(items)
        else:
            print_table(items, LIST_COLUMNS, title="Tickets")
    except SystemExit:
        raise
    except Exception as e:
        handle_api_error(e)


@app.command("get")
def get_cmd(
    id: int = typer.Argument(..., help="Ticket ID."),
    json_output: bool = JSON_OPTION,
) -> None:
    """Get a single ticket by ID."""
    _set_json(json_output)
    try:
        client = get_client()
        item = client.tickets.get(id)
        data = _model_to_dict(item)
        if state.json_output:
            print_json(data)
        else:
            print_detail(data, DETAIL_COLUMNS)
    except SystemExit:
        raise
    except Exception as e:
        handle_api_error(e)


@app.command("create")
def create_cmd(
    summary: str = typer.Option(..., "--summary", help="Ticket summary."),
    client_id: Optional[int] = typer.Option(None, "--client-id", help="Client ID."),
    tickettype_id: Optional[int] = typer.Option(None, "--tickettype-id", help="Ticket type ID."),
    details: Optional[str] = typer.Option(None, "--details", help="Ticket details."),
    priority_id: Optional[int] = typer.Option(None, "--priority-id", help="Priority ID."),
    agent_id: Optional[int] = typer.Option(None, "--agent-id", help="Agent ID."),
    team_id: Optional[int] = typer.Option(None, "--team-id", help="Team ID."),
    user_id: Optional[int] = typer.Option(None, "--user-id", help="User ID."),
    site_id: Optional[int] = typer.Option(None, "--site-id", help="Site ID."),
    data: Optional[str] = typer.Option(None, "--data", "-d", help="Extra fields as JSON."),
    json_output: bool = JSON_OPTION,
) -> None:
    """Create a new ticket."""
    _set_json(json_output)
    body: dict[str, Any] = {"summary": summary}
    for key, val in {
        "client_id": client_id, "tickettype_id": tickettype_id,
        "details": details, "priority_id": priority_id,
        "agent_id": agent_id, "team_id": team_id,
        "user_id": user_id, "site_id": site_id,
    }.items():
        if val is not None:
            body[key] = val

    if data:
        try:
            body.update(json.loads(data))
        except json.JSONDecodeError as e:
            from .._output import print_error
            print_error(f"Invalid JSON: {e}")
            raise typer.Exit(1)

    try:
        client = get_client()
        item = client.tickets.create(body)
        result = _model_to_dict(item)
        if state.json_output:
            print_json(result)
        else:
            print_detail(result, DETAIL_COLUMNS)
    except SystemExit:
        raise
    except Exception as e:
        handle_api_error(e)


@app.command("update")
def update_cmd(
    id: int = typer.Argument(..., help="Ticket ID."),
    summary: Optional[str] = typer.Option(None, "--summary", help="New summary."),
    status_id: Optional[int] = typer.Option(None, "--status-id", help="New status ID."),
    agent_id: Optional[int] = typer.Option(None, "--agent-id", help="New agent ID."),
    team_id: Optional[int] = typer.Option(None, "--team-id", help="New team ID."),
    priority_id: Optional[int] = typer.Option(None, "--priority-id", help="New priority ID."),
    data: Optional[str] = typer.Option(None, "--data", "-d", help="Extra fields as JSON."),
    json_output: bool = JSON_OPTION,
) -> None:
    """Update an existing ticket."""
    _set_json(json_output)
    body: dict[str, Any] = {"id": id}
    for key, val in {
        "summary": summary, "status_id": status_id,
        "agent_id": agent_id, "team_id": team_id,
        "priority_id": priority_id,
    }.items():
        if val is not None:
            body[key] = val

    if data:
        try:
            body.update(json.loads(data))
        except json.JSONDecodeError as e:
            from .._output import print_error
            print_error(f"Invalid JSON: {e}")
            raise typer.Exit(1)

    try:
        client = get_client()
        item = client.tickets.update(body)
        result = _model_to_dict(item)
        if state.json_output:
            print_json(result)
        else:
            print_detail(result, DETAIL_COLUMNS)
    except SystemExit:
        raise
    except Exception as e:
        handle_api_error(e)


@app.command("delete")
def delete_cmd(
    id: int = typer.Argument(..., help="Ticket ID."),
    confirm: bool = typer.Option(False, "--yes", "-y", help="Skip confirmation."),
    json_output: bool = JSON_OPTION,
) -> None:
    """Delete a ticket."""
    _set_json(json_output)
    if not confirm:
        typer.confirm(f"Delete ticket {id}?", abort=True)
    try:
        client = get_client()
        client.tickets.delete(id)
        if state.json_output:
            print_json({"deleted": True, "id": id})
        else:
            typer.echo(f"Deleted ticket {id}.")
    except SystemExit:
        raise
    except Exception as e:
        handle_api_error(e)
