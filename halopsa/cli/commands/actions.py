"""Actions command with typed filters."""

from __future__ import annotations

import json
from typing import Any, Optional

import typer

from .._app import get_client, handle_api_error, state
from .._output import print_detail, print_json, print_table
from .._resource_cmd import JSON_OPTION, _model_to_dict, _set_json

LIST_COLUMNS = ["id", "ticket_id", "outcome", "who", "datetime", "note", "timetaken"]
DETAIL_COLUMNS = [
    "id", "ticket_id", "outcome", "outcome_id", "who", "who_agentid", "who_type",
    "datetime", "last_updated", "note", "emailfrom", "emailto", "emailcc",
    "hiddenfromuser", "timetaken", "important", "new_status", "sendemail",
]

app = typer.Typer(name="actions", help="Manage actions.", no_args_is_help=True)


@app.command("list")
def list_cmd(
    page_size: int = typer.Option(50, "--page-size", "-n", help="Results per page."),
    page_no: int = typer.Option(1, "--page", "-p", help="Page number."),
    ticket_id: Optional[int] = typer.Option(None, "--ticket-id", help="Filter by ticket ID."),
    agent_id: Optional[int] = typer.Option(None, "--agent-id", help="Filter by agent ID."),
    exclude_sys: Optional[bool] = typer.Option(None, "--exclude-sys", help="Exclude system actions."),
    all_pages: bool = typer.Option(False, "--all", help="Fetch all pages."),
    json_output: bool = JSON_OPTION,
) -> None:
    """List actions with optional filters."""
    _set_json(json_output)
    try:
        client = get_client()
        kwargs: dict[str, Any] = {}
        if ticket_id is not None:
            kwargs["ticket_id"] = ticket_id
        if agent_id is not None:
            kwargs["agent_id"] = agent_id
        if exclude_sys is not None:
            kwargs["excludesys"] = exclude_sys

        if all_pages:
            items_raw = list(client.actions.list_all(page_size=page_size, **kwargs))
            items = [_model_to_dict(i) for i in items_raw]
        else:
            result = client.actions.list(page_size=page_size, page_no=page_no, **kwargs)
            items = [_model_to_dict(i) for i in result.items]

        if state.json_output:
            print_json(items)
        else:
            print_table(items, LIST_COLUMNS, title="Actions")
    except SystemExit:
        raise
    except Exception as e:
        handle_api_error(e)


@app.command("get")
def get_cmd(
    id: int = typer.Argument(..., help="Action ID."),
    json_output: bool = JSON_OPTION,
) -> None:
    """Get a single action by ID."""
    _set_json(json_output)
    try:
        client = get_client()
        item = client.actions.get(id)
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
    ticket_id: int = typer.Option(..., "--ticket-id", help="Ticket ID for the action."),
    note: Optional[str] = typer.Option(None, "--note", help="Action note."),
    outcome: Optional[str] = typer.Option(None, "--outcome", help="Outcome text."),
    data: Optional[str] = typer.Option(None, "--data", "-d", help="Extra fields as JSON."),
    json_output: bool = JSON_OPTION,
) -> None:
    """Create a new action."""
    _set_json(json_output)
    body: dict[str, Any] = {"ticket_id": ticket_id}
    if note is not None:
        body["note"] = note
    if outcome is not None:
        body["outcome"] = outcome
    if data:
        try:
            body.update(json.loads(data))
        except json.JSONDecodeError as e:
            from .._output import print_error
            print_error(f"Invalid JSON: {e}")
            raise typer.Exit(1)
    try:
        client = get_client()
        item = client.actions.create(body)
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
    id: int = typer.Argument(..., help="Action ID."),
    data: str = typer.Option(..., "--data", "-d", help="JSON with fields to update."),
    json_output: bool = JSON_OPTION,
) -> None:
    """Update an existing action."""
    _set_json(json_output)
    try:
        body = json.loads(data)
    except json.JSONDecodeError as e:
        from .._output import print_error
        print_error(f"Invalid JSON: {e}")
        raise typer.Exit(1)
    body["id"] = id
    try:
        client = get_client()
        item = client.actions.update(body)
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
    id: int = typer.Argument(..., help="Action ID."),
    confirm: bool = typer.Option(False, "--yes", "-y", help="Skip confirmation."),
    json_output: bool = JSON_OPTION,
) -> None:
    """Delete an action."""
    _set_json(json_output)
    if not confirm:
        typer.confirm(f"Delete action {id}?", abort=True)
    try:
        client = get_client()
        client.actions.delete(id)
        if state.json_output:
            print_json({"deleted": True, "id": id})
        else:
            typer.echo(f"Deleted action {id}.")
    except SystemExit:
        raise
    except Exception as e:
        handle_api_error(e)
