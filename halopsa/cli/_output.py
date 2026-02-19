"""Rich table and JSON output formatting."""

from __future__ import annotations

import json as _json
from typing import Any

from rich.console import Console
from rich.table import Table
from rich.text import Text

console = Console()
err_console = Console(stderr=True)


def print_table(
    items: list[dict[str, Any]],
    columns: list[str],
    title: str | None = None,
) -> None:
    """Print a list of items as a Rich table."""
    if not items:
        console.print("[dim]No results.[/dim]")
        return

    table = Table(title=title, show_lines=False, pad_edge=False)
    for col in columns:
        table.add_column(col, overflow="fold")

    for item in items:
        row = [_fmt(item.get(col)) for col in columns]
        table.add_row(*row)

    console.print(table)


def print_detail(item: dict[str, Any], columns: list[str] | None = None) -> None:
    """Print a single item as a key-value table."""
    if columns is None:
        columns = [k for k in item if item[k] is not None]

    table = Table(show_header=False, pad_edge=False, box=None)
    table.add_column("Field", style="bold cyan", min_width=20)
    table.add_column("Value")

    for col in columns:
        val = item.get(col)
        if val is not None:
            table.add_row(col, _fmt(val))

    console.print(table)


def print_json(data: Any) -> None:
    """Pretty-print data as JSON."""
    console.print_json(_json.dumps(data, default=str))


def print_error(msg: str) -> None:
    """Print an error message to stderr."""
    err_console.print(f"[bold red]Error:[/bold red] {msg}")


def _fmt(val: Any) -> str:
    """Format a value for table display."""
    if val is None:
        return ""
    if isinstance(val, bool):
        return "Yes" if val else "No"
    if isinstance(val, list):
        if not val:
            return ""
        return ", ".join(str(v) for v in val[:5])
    return str(val)
