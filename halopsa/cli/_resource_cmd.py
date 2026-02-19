"""Generic resource command factory — generates list/get/create/update/delete for any resource."""

from __future__ import annotations

import json
from typing import Any, Optional

import typer

from ._app import get_client, handle_api_error, state
from ._output import print_detail, print_error, print_json, print_table


# Reusable --json option for any command
JSON_OPTION = typer.Option(False, "--json", help="Output as JSON.", is_eager=True)


def _set_json(value: bool) -> None:
    if value:
        state.json_output = True


def make_resource_app(
    name: str,
    resource_attr: str,
    list_columns: list[str],
    detail_columns: list[str] | None = None,
    *,
    no_delete: bool = False,
) -> typer.Typer:
    """Create a Typer sub-app with standard CRUD commands for a resource.

    Args:
        name: Display name (e.g. "tickets").
        resource_attr: Attribute name on HaloClient (e.g. "tickets").
        list_columns: Columns to show in list table view.
        detail_columns: Columns to show in detail view (None = all non-null).
        no_delete: If True, skip generating the delete command.
    """
    resource_app = typer.Typer(
        name=name,
        help=f"Manage {name}.",
        no_args_is_help=True,
    )

    @resource_app.command("list")
    def list_cmd(
        page_size: int = typer.Option(50, "--page-size", "-n", help="Results per page."),
        page_no: int = typer.Option(1, "--page", "-p", help="Page number."),
        search: Optional[str] = typer.Option(None, "--search", "-s", help="Search term."),
        all_pages: bool = typer.Option(False, "--all", help="Fetch all pages."),
        json_output: bool = JSON_OPTION,
    ) -> None:
        """List resources."""
        _set_json(json_output)
        try:
            client = get_client()
            resource = getattr(client, resource_attr)
            kwargs: dict[str, Any] = {}
            if search:
                kwargs["search"] = search

            if all_pages:
                items_raw: list[Any] = []
                for item in resource.list_all(page_size=page_size, **kwargs):
                    items_raw.append(item)
                items = [_model_to_dict(i) for i in items_raw]
            else:
                result = resource.list(page_size=page_size, page_no=page_no, **kwargs)
                items = [_model_to_dict(i) for i in result.items]

            if state.json_output:
                print_json(items)
            else:
                print_table(items, list_columns, title=name.title())
        except SystemExit:
            raise
        except Exception as e:
            handle_api_error(e)

    @resource_app.command("get")
    def get_cmd(
        id: int = typer.Argument(..., help="Resource ID."),
        json_output: bool = JSON_OPTION,
    ) -> None:
        """Get a single resource by ID."""
        _set_json(json_output)
        try:
            client = get_client()
            resource = getattr(client, resource_attr)
            item = resource.get(id)
            data = _model_to_dict(item)
            if state.json_output:
                print_json(data)
            else:
                print_detail(data, detail_columns)
        except SystemExit:
            raise
        except Exception as e:
            handle_api_error(e)

    @resource_app.command("create")
    def create_cmd(
        data: str = typer.Option(..., "--data", "-d", help="JSON object for creation."),
        json_output: bool = JSON_OPTION,
    ) -> None:
        """Create a new resource from JSON."""
        _set_json(json_output)
        try:
            body = json.loads(data)
        except json.JSONDecodeError as e:
            print_error(f"Invalid JSON: {e}")
            raise typer.Exit(1)
        try:
            client = get_client()
            resource = getattr(client, resource_attr)
            item = resource.create(body)
            result = _model_to_dict(item)
            if state.json_output:
                print_json(result)
            else:
                print_detail(result, detail_columns)
        except SystemExit:
            raise
        except Exception as e:
            handle_api_error(e)

    @resource_app.command("update")
    def update_cmd(
        id: int = typer.Argument(..., help="Resource ID."),
        data: str = typer.Option(..., "--data", "-d", help="JSON object with fields to update."),
        json_output: bool = JSON_OPTION,
    ) -> None:
        """Update an existing resource from JSON."""
        _set_json(json_output)
        try:
            body = json.loads(data)
        except json.JSONDecodeError as e:
            print_error(f"Invalid JSON: {e}")
            raise typer.Exit(1)
        body["id"] = id
        try:
            client = get_client()
            resource = getattr(client, resource_attr)
            item = resource.update(body)
            result = _model_to_dict(item)
            if state.json_output:
                print_json(result)
            else:
                print_detail(result, detail_columns)
        except SystemExit:
            raise
        except Exception as e:
            handle_api_error(e)

    if not no_delete:

        @resource_app.command("delete")
        def delete_cmd(
            id: int = typer.Argument(..., help="Resource ID."),
            confirm: bool = typer.Option(False, "--yes", "-y", help="Skip confirmation."),
            json_output: bool = JSON_OPTION,
        ) -> None:
            """Delete a resource by ID."""
            _set_json(json_output)
            if not confirm:
                typer.confirm(f"Delete {name.rstrip('s')} {id}?", abort=True)
            try:
                client = get_client()
                resource = getattr(client, resource_attr)
                resource.delete(id)
                if state.json_output:
                    print_json({"deleted": True, "id": id})
                else:
                    typer.echo(f"Deleted {name.rstrip('s')} {id}.")
            except SystemExit:
                raise
            except Exception as e:
                handle_api_error(e)

    return resource_app


def _model_to_dict(item: Any) -> dict[str, Any]:
    """Convert a Pydantic model to dict."""
    if hasattr(item, "model_dump"):
        return item.model_dump()
    return dict(item)
