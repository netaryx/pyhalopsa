"""Generic API request escape hatch."""

from __future__ import annotations

import json
from typing import Any, Optional

import typer

from .._app import get_client, handle_api_error, state
from .._output import print_json, print_error

app = typer.Typer(name="request", help="Make a raw API request.")


@app.callback(invoke_without_command=True)
def request_cmd(
    ctx: typer.Context,
    method: str = typer.Argument(..., help="HTTP method (GET, POST, DELETE, etc.)."),
    path: str = typer.Argument(..., help="API path (e.g. /Tickets, /Agent/me)."),
    param: Optional[list[str]] = typer.Option(
        None, "--param", "-p", help="Query parameter as key=value. Repeatable."
    ),
    data: Optional[str] = typer.Option(
        None, "--data", "-d", help="JSON request body."
    ),
) -> None:
    """Execute a raw API request.

    Examples:
        halo request GET /Tickets --param page_size=5
        halo request POST /Tickets --data '{"summary": "Test"}'
    """
    params: dict[str, str] = {}
    if param:
        for p in param:
            if "=" not in p:
                print_error(f"Invalid param format '{p}', expected key=value")
                raise typer.Exit(1)
            k, v = p.split("=", 1)
            params[k] = v

    json_body: Any = None
    if data:
        try:
            json_body = json.loads(data)
        except json.JSONDecodeError as e:
            print_error(f"Invalid JSON: {e}")
            raise typer.Exit(1)

    try:
        client = get_client()
        result = client.request(
            method.upper(),
            path.lstrip("/"),
            params=params or None,
            json_body=json_body,
        )
        print_json(result if result is not None else {"status": "ok"})
    except SystemExit:
        raise
    except Exception as e:
        handle_api_error(e)
