"""Sync and async HaloPSA client implementations."""

from __future__ import annotations

import asyncio
from typing import Any, TypeVar

import httpx
from pydantic import BaseModel

from ._base_client import _BaseClientMixin
from ._transport import _AsyncTransport, _SyncTransport
from .auth import TokenManager
from .exceptions import HaloAuthenticationError, HaloTimeoutError

T = TypeVar("T", bound=BaseModel)


class HaloClient(_BaseClientMixin):
    """Synchronous HaloPSA API client."""

    def __init__(
        self,
        *,
        tenant_url: str,
        client_id: str,
        client_secret: str,
        scope: str = "all",
        tenant: str | None = None,
        auth_url: str | None = None,
        timeout: float = 30.0,
        max_retries: int = 3,
        retry_backoff_factor: float = 1.0,
    ) -> None:
        self.base_url = tenant_url.rstrip("/")
        self.max_retries = max_retries
        self.retry_backoff_factor = retry_backoff_factor

        token_url = auth_url or f"{self.base_url}/auth/token"
        self._token_mgr = TokenManager(
            token_url=token_url,
            client_id=client_id,
            client_secret=client_secret,
            scope=scope,
            tenant=tenant,
        )
        self._transport = _SyncTransport(timeout=timeout)
        self._init_resources()

    def _init_resources(self) -> None:
        from .resources.tickets import TicketsResource
        from .resources.actions import ActionsResource
        from .resources.clients import ClientsResource
        from .resources.users import UsersResource
        from .resources.agents import AgentsResource
        from .resources.assets import AssetsResource
        from .resources.sites import SitesResource
        from .resources.invoices import InvoicesResource
        from .resources.contracts import ContractsResource
        from .resources.opportunities import OpportunitiesResource
        from .resources.projects import ProjectsResource
        from .resources.appointments import AppointmentsResource
        from .resources.items import ItemsResource
        from .resources.kb_articles import KBArticlesResource
        from .resources.suppliers import SuppliersResource
        from .resources.attachments import AttachmentsResource
        from .resources.statuses import StatusesResource
        from .resources.teams import TeamsResource
        from .resources.categories import CategoriesResource
        from .resources.priorities import PrioritiesResource
        from .resources.slas import SLAsResource
        from .resources.ticket_types import TicketTypesResource
        from .resources.top_levels import TopLevelsResource
        from .resources.expenses import ExpensesResource
        from .resources.timesheets import TimesheetsResource
        from .resources.releases import ReleasesResource
        from .resources.reports import ReportsResource
        from .resources.webhooks import WebhooksResource
        from .resources.workdays import WorkdaysResource
        from .resources.software_licences import SoftwareLicencesResource
        from .resources.crm_notes import CRMNotesResource
        from .resources.quotations import QuotationsResource

        self.tickets = TicketsResource(self)
        self.actions = ActionsResource(self)
        self.clients = ClientsResource(self)
        self.users = UsersResource(self)
        self.agents = AgentsResource(self)
        self.assets = AssetsResource(self)
        self.sites = SitesResource(self)
        self.invoices = InvoicesResource(self)
        self.contracts = ContractsResource(self)
        self.opportunities = OpportunitiesResource(self)
        self.projects = ProjectsResource(self)
        self.appointments = AppointmentsResource(self)
        self.items = ItemsResource(self)
        self.kb_articles = KBArticlesResource(self)
        self.suppliers = SuppliersResource(self)
        self.attachments = AttachmentsResource(self)
        self.statuses = StatusesResource(self)
        self.teams = TeamsResource(self)
        self.categories = CategoriesResource(self)
        self.priorities = PrioritiesResource(self)
        self.slas = SLAsResource(self)
        self.ticket_types = TicketTypesResource(self)
        self.top_levels = TopLevelsResource(self)
        self.expenses = ExpensesResource(self)
        self.timesheets = TimesheetsResource(self)
        self.releases = ReleasesResource(self)
        self.reports = ReportsResource(self)
        self.webhooks = WebhooksResource(self)
        self.workdays = WorkdaysResource(self)
        self.software_licences = SoftwareLicencesResource(self)
        self.crm_notes = CRMNotesResource(self)
        self.quotations = QuotationsResource(self)

    def request(
        self,
        method: str,
        path: str,
        *,
        params: dict[str, Any] | None = None,
        json_body: Any | None = None,
        response_model: type[T] | None = None,
    ) -> Any:
        """Execute an API request with auto-auth, retry, and error mapping."""
        url = self._build_url(path)
        params = self._clean_params(params)

        token = self._token_mgr.get_token(self._transport.client)
        headers = {"Authorization": f"Bearer {token}"}

        last_resp: httpx.Response | None = None
        for attempt in range(1, self.max_retries + 2):
            try:
                resp = self._transport.send(
                    method, url, headers=headers, params=params, json_body=json_body
                )
            except httpx.TimeoutException as exc:
                raise HaloTimeoutError(str(exc)) from exc

            if resp.status_code < 300:
                return self._handle_success(resp, response_model)

            # 401 → refresh token and retry once
            if resp.status_code == 401 and attempt == 1:
                token = self._token_mgr.force_refresh(self._transport.client)
                headers["Authorization"] = f"Bearer {token}"
                continue

            if self._should_retry(resp, attempt):
                self._sleep_sync(self._backoff(resp, attempt))
                continue

            last_resp = resp
            break

        raise self._map_error(last_resp or resp)

    @staticmethod
    def _handle_success(resp: httpx.Response, model: type[T] | None = None) -> Any:
        if resp.status_code == 204 or not resp.content:
            return None
        data = resp.json()
        if model is not None:
            return model.model_validate(data)
        return data

    def close(self) -> None:
        self._transport.close()

    def __enter__(self) -> HaloClient:
        return self

    def __exit__(self, *args: Any) -> None:
        self.close()


class AsyncHaloClient(_BaseClientMixin):
    """Asynchronous HaloPSA API client."""

    def __init__(
        self,
        *,
        tenant_url: str,
        client_id: str,
        client_secret: str,
        scope: str = "all",
        tenant: str | None = None,
        auth_url: str | None = None,
        timeout: float = 30.0,
        max_retries: int = 3,
        retry_backoff_factor: float = 1.0,
    ) -> None:
        self.base_url = tenant_url.rstrip("/")
        self.max_retries = max_retries
        self.retry_backoff_factor = retry_backoff_factor

        token_url = auth_url or f"{self.base_url}/auth/token"
        self._token_mgr = TokenManager(
            token_url=token_url,
            client_id=client_id,
            client_secret=client_secret,
            scope=scope,
            tenant=tenant,
        )
        self._transport = _AsyncTransport(timeout=timeout)
        self._init_resources()

    def _init_resources(self) -> None:
        from .resources.tickets import TicketsResource
        from .resources.actions import ActionsResource
        from .resources.clients import ClientsResource
        from .resources.users import UsersResource
        from .resources.agents import AgentsResource
        from .resources.assets import AssetsResource
        from .resources.sites import SitesResource
        from .resources.invoices import InvoicesResource
        from .resources.contracts import ContractsResource
        from .resources.opportunities import OpportunitiesResource
        from .resources.projects import ProjectsResource
        from .resources.appointments import AppointmentsResource
        from .resources.items import ItemsResource
        from .resources.kb_articles import KBArticlesResource
        from .resources.suppliers import SuppliersResource
        from .resources.attachments import AttachmentsResource
        from .resources.statuses import StatusesResource
        from .resources.teams import TeamsResource
        from .resources.categories import CategoriesResource
        from .resources.priorities import PrioritiesResource
        from .resources.slas import SLAsResource
        from .resources.ticket_types import TicketTypesResource
        from .resources.top_levels import TopLevelsResource
        from .resources.expenses import ExpensesResource
        from .resources.timesheets import TimesheetsResource
        from .resources.releases import ReleasesResource
        from .resources.reports import ReportsResource
        from .resources.webhooks import WebhooksResource
        from .resources.workdays import WorkdaysResource
        from .resources.software_licences import SoftwareLicencesResource
        from .resources.crm_notes import CRMNotesResource
        from .resources.quotations import QuotationsResource

        self.tickets = TicketsResource(self)
        self.actions = ActionsResource(self)
        self.clients = ClientsResource(self)
        self.users = UsersResource(self)
        self.agents = AgentsResource(self)
        self.assets = AssetsResource(self)
        self.sites = SitesResource(self)
        self.invoices = InvoicesResource(self)
        self.contracts = ContractsResource(self)
        self.opportunities = OpportunitiesResource(self)
        self.projects = ProjectsResource(self)
        self.appointments = AppointmentsResource(self)
        self.items = ItemsResource(self)
        self.kb_articles = KBArticlesResource(self)
        self.suppliers = SuppliersResource(self)
        self.attachments = AttachmentsResource(self)
        self.statuses = StatusesResource(self)
        self.teams = TeamsResource(self)
        self.categories = CategoriesResource(self)
        self.priorities = PrioritiesResource(self)
        self.slas = SLAsResource(self)
        self.ticket_types = TicketTypesResource(self)
        self.top_levels = TopLevelsResource(self)
        self.expenses = ExpensesResource(self)
        self.timesheets = TimesheetsResource(self)
        self.releases = ReleasesResource(self)
        self.reports = ReportsResource(self)
        self.webhooks = WebhooksResource(self)
        self.workdays = WorkdaysResource(self)
        self.software_licences = SoftwareLicencesResource(self)
        self.crm_notes = CRMNotesResource(self)
        self.quotations = QuotationsResource(self)

    async def arequest(
        self,
        method: str,
        path: str,
        *,
        params: dict[str, Any] | None = None,
        json_body: Any | None = None,
        response_model: type[T] | None = None,
    ) -> Any:
        """Execute an async API request with auto-auth, retry, and error mapping."""
        url = self._build_url(path)
        params = self._clean_params(params)

        token = await self._token_mgr.aget_token(self._transport.client)
        headers = {"Authorization": f"Bearer {token}"}

        last_resp: httpx.Response | None = None
        for attempt in range(1, self.max_retries + 2):
            try:
                resp = await self._transport.send(
                    method, url, headers=headers, params=params, json_body=json_body
                )
            except httpx.TimeoutException as exc:
                raise HaloTimeoutError(str(exc)) from exc

            if resp.status_code < 300:
                return self._handle_success(resp, response_model)

            if resp.status_code == 401 and attempt == 1:
                token = await self._token_mgr.aforce_refresh(self._transport.client)
                headers["Authorization"] = f"Bearer {token}"
                continue

            if self._should_retry(resp, attempt):
                await asyncio.sleep(self._backoff(resp, attempt))
                continue

            last_resp = resp
            break

        raise self._map_error(last_resp or resp)

    # Also expose sync-style `request()` alias for the generic escape hatch
    def request(
        self,
        method: str,
        path: str,
        *,
        params: dict[str, Any] | None = None,
        json_body: Any | None = None,
        response_model: type[T] | None = None,
    ) -> Any:
        """Sync alias — raises error; use ``arequest`` in async context."""
        raise RuntimeError(
            "Use 'await client.arequest(...)' with AsyncHaloClient. "
            "For synchronous usage, use HaloClient instead."
        )

    @staticmethod
    def _handle_success(resp: httpx.Response, model: type[T] | None = None) -> Any:
        if resp.status_code == 204 or not resp.content:
            return None
        data = resp.json()
        if model is not None:
            return model.model_validate(data)
        return data

    async def close(self) -> None:
        await self._transport.close()

    async def __aenter__(self) -> AsyncHaloClient:
        return self

    async def __aexit__(self, *args: Any) -> None:
        await self.close()
