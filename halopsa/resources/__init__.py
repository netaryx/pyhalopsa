"""HaloPSA resource classes."""

from .tickets import TicketsResource
from .actions import ActionsResource
from .clients import ClientsResource
from .users import UsersResource
from .agents import AgentsResource
from .assets import AssetsResource
from .sites import SitesResource
from .invoices import InvoicesResource
from .contracts import ContractsResource
from .opportunities import OpportunitiesResource
from .projects import ProjectsResource
from .appointments import AppointmentsResource
from .items import ItemsResource
from .kb_articles import KBArticlesResource
from .suppliers import SuppliersResource
from .attachments import AttachmentsResource
from .statuses import StatusesResource
from .teams import TeamsResource
from .categories import CategoriesResource
from .priorities import PrioritiesResource
from .slas import SLAsResource
from .ticket_types import TicketTypesResource
from .top_levels import TopLevelsResource
from .expenses import ExpensesResource
from .timesheets import TimesheetsResource
from .releases import ReleasesResource
from .reports import ReportsResource
from .webhooks import WebhooksResource
from .workdays import WorkdaysResource
from .software_licences import SoftwareLicencesResource
from .crm_notes import CRMNotesResource
from .quotations import QuotationsResource

__all__ = [
    "TicketsResource",
    "ActionsResource",
    "ClientsResource",
    "UsersResource",
    "AgentsResource",
    "AssetsResource",
    "SitesResource",
    "InvoicesResource",
    "ContractsResource",
    "OpportunitiesResource",
    "ProjectsResource",
    "AppointmentsResource",
    "ItemsResource",
    "KBArticlesResource",
    "SuppliersResource",
    "AttachmentsResource",
    "StatusesResource",
    "TeamsResource",
    "CategoriesResource",
    "PrioritiesResource",
    "SLAsResource",
    "TicketTypesResource",
    "TopLevelsResource",
    "ExpensesResource",
    "TimesheetsResource",
    "ReleasesResource",
    "ReportsResource",
    "WebhooksResource",
    "WorkdaysResource",
    "SoftwareLicencesResource",
    "CRMNotesResource",
    "QuotationsResource",
]
