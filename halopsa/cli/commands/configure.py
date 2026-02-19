"""Interactive config file setup."""

from __future__ import annotations

import typer

from .._config import CONFIG_FILE, save_config

app = typer.Typer(name="configure", help="Set up HaloPSA credentials.")


@app.callback(invoke_without_command=True)
def configure(ctx: typer.Context) -> None:
    """Interactive setup — saves credentials to ~/.halopsa/config.yaml."""
    if ctx.invoked_subcommand is not None:
        return

    typer.echo("HaloPSA CLI Configuration")
    typer.echo("=" * 40)

    tenant_url = typer.prompt("Tenant URL (e.g. https://company.halopsa.com)")
    client_id = typer.prompt("Client ID")
    client_secret = typer.prompt("Client Secret", hide_input=True)
    scope = typer.prompt("Scope", default="all")
    tenant = typer.prompt("Tenant (optional, press Enter to skip)", default="")

    data = {
        "tenant_url": tenant_url,
        "client_id": client_id,
        "client_secret": client_secret,
        "scope": scope,
    }
    if tenant:
        data["tenant"] = tenant

    path = save_config(data)
    typer.echo(f"\nConfig saved to {path}")


@app.command("show")
def show() -> None:
    """Show the current config file path and status."""
    if CONFIG_FILE.exists():
        typer.echo(f"Config file: {CONFIG_FILE}")
        typer.echo("Status: configured")
    else:
        typer.echo(f"Config file: {CONFIG_FILE}")
        typer.echo("Status: not configured")
        typer.echo("Run 'halo configure' to set up credentials.")


@app.command("path")
def path() -> None:
    """Print the config file path."""
    typer.echo(str(CONFIG_FILE))
