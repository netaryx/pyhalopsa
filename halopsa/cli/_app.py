"""Main Typer app, global options, and client factory."""

from __future__ import annotations

from typing import Any, Optional

import typer

from .._version import __version__
from ._config import HaloConfig, resolve_config
from ._output import print_error

app = typer.Typer(
    name="halo",
    help="HaloPSA CLI — manage your HaloPSA instance from the command line.",
    no_args_is_help=True,
    rich_markup_mode="rich",
)


# ── Global state ───────────────────────────────────────────────────────────

class _State:
    """Mutable global state set by the callback."""

    tenant_url: str | None = None
    client_id: str | None = None
    client_secret: str | None = None
    json_output: bool = False
    no_color: bool = False


state = _State()


def _version_callback(value: bool) -> None:
    if value:
        typer.echo(f"halopsa {__version__}")
        raise typer.Exit()


@app.callback()
def main(
    tenant_url: Optional[str] = typer.Option(
        None, "--tenant-url", envvar="HALO_TENANT_URL", help="HaloPSA tenant URL."
    ),
    client_id: Optional[str] = typer.Option(
        None, "--client-id", envvar="HALO_CLIENT_ID", help="OAuth client ID."
    ),
    client_secret: Optional[str] = typer.Option(
        None, "--client-secret", envvar="HALO_CLIENT_SECRET", help="OAuth client secret."
    ),
    json_output: bool = typer.Option(False, "--json", help="Output as JSON."),
    no_color: bool = typer.Option(False, "--no-color", help="Disable colored output."),
    version: Optional[bool] = typer.Option(
        None, "--version", "-v", help="Show version and exit.",
        callback=_version_callback, is_eager=True,
    ),
) -> None:
    """HaloPSA CLI."""
    state.tenant_url = tenant_url
    state.client_id = client_id
    state.client_secret = client_secret
    state.json_output = json_output
    state.no_color = no_color


def get_client() -> Any:
    """Build a HaloClient from resolved config. Exits on error."""
    from ..client import HaloClient

    cfg = resolve_config(
        tenant_url=state.tenant_url,
        client_id=state.client_id,
        client_secret=state.client_secret,
    )
    if not cfg.is_complete:
        missing = []
        if not cfg.tenant_url:
            missing.append("tenant_url")
        if not cfg.client_id:
            missing.append("client_id")
        if not cfg.client_secret:
            missing.append("client_secret")
        print_error(
            f"Missing credentials: {', '.join(missing)}. "
            "Set via --flags, env vars (HALO_TENANT_URL, HALO_CLIENT_ID, HALO_CLIENT_SECRET), "
            "or run 'halo configure'."
        )
        raise typer.Exit(1)

    return HaloClient(
        tenant_url=cfg.tenant_url,
        client_id=cfg.client_id,
        client_secret=cfg.client_secret,
        scope=cfg.scope,
        tenant=cfg.tenant,
    )


def handle_api_error(e: Exception) -> None:
    """Print an API error and exit."""
    print_error(str(e))
    raise typer.Exit(1)


# ── Register all sub-commands ─────────────────────────────────────────────

def _register_commands() -> None:
    from .commands.tickets import app as tickets_app
    from .commands.actions import app as actions_app
    from .commands.clients import app as clients_app
    from .commands.users import app as users_app
    from .commands.agents import app as agents_app
    from .commands.assets import app as assets_app
    from .commands.sites import app as sites_app
    from .commands.invoices import app as invoices_app
    from .commands.contracts import app as contracts_app
    from .commands.opportunities import app as opportunities_app
    from .commands.projects import app as projects_app
    from .commands.appointments import app as appointments_app
    from .commands.items import app as items_app
    from .commands.kb_articles import app as kb_articles_app
    from .commands.suppliers import app as suppliers_app
    from .commands.attachments import app as attachments_app
    from .commands.statuses import app as statuses_app
    from .commands.teams import app as teams_app
    from .commands.categories import app as categories_app
    from .commands.priorities import app as priorities_app
    from .commands.slas import app as slas_app
    from .commands.ticket_types import app as ticket_types_app
    from .commands.top_levels import app as top_levels_app
    from .commands.expenses import app as expenses_app
    from .commands.timesheets import app as timesheets_app
    from .commands.releases import app as releases_app
    from .commands.reports import app as reports_app
    from .commands.webhooks import app as webhooks_app
    from .commands.workdays import app as workdays_app
    from .commands.software_licences import app as software_licences_app
    from .commands.crm_notes import app as crm_notes_app
    from .commands.quotations import app as quotations_app
    from .commands.request import app as request_app
    from .commands.configure import app as configure_app

    app.add_typer(tickets_app, name="tickets")
    app.add_typer(actions_app, name="actions")
    app.add_typer(clients_app, name="clients")
    app.add_typer(users_app, name="users")
    app.add_typer(agents_app, name="agents")
    app.add_typer(assets_app, name="assets")
    app.add_typer(sites_app, name="sites")
    app.add_typer(invoices_app, name="invoices")
    app.add_typer(contracts_app, name="contracts")
    app.add_typer(opportunities_app, name="opportunities")
    app.add_typer(projects_app, name="projects")
    app.add_typer(appointments_app, name="appointments")
    app.add_typer(items_app, name="items")
    app.add_typer(kb_articles_app, name="kb-articles")
    app.add_typer(suppliers_app, name="suppliers")
    app.add_typer(attachments_app, name="attachments")
    app.add_typer(statuses_app, name="statuses")
    app.add_typer(teams_app, name="teams")
    app.add_typer(categories_app, name="categories")
    app.add_typer(priorities_app, name="priorities")
    app.add_typer(slas_app, name="slas")
    app.add_typer(ticket_types_app, name="ticket-types")
    app.add_typer(top_levels_app, name="top-levels")
    app.add_typer(expenses_app, name="expenses")
    app.add_typer(timesheets_app, name="timesheets")
    app.add_typer(releases_app, name="releases")
    app.add_typer(reports_app, name="reports")
    app.add_typer(webhooks_app, name="webhooks")
    app.add_typer(workdays_app, name="workdays")
    app.add_typer(software_licences_app, name="software-licences")
    app.add_typer(crm_notes_app, name="crm-notes")
    app.add_typer(quotations_app, name="quotations")
    app.add_typer(request_app, name="request")
    app.add_typer(configure_app, name="configure")


_register_commands()
