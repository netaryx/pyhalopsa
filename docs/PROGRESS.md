# HaloPSA Python SDK & CLI — Progress Tracker

**SDK: 32 typed resources implemented | CLI: 34 commands (32 resources + configure + request)**

---

## Implementation Phases

### Phase 1: Foundation ✅
- [x] `halopsa/exceptions.py` — Exception hierarchy
- [x] `halopsa/models/_base.py` — HaloModel base + PaginatedResponse
- [x] `halopsa/models/_common.py` — CustomField + shared types
- [x] `halopsa/auth.py` — TokenManager (OAuth2 client_credentials)
- [x] `halopsa/_transport.py` — _SyncTransport + _AsyncTransport
- [x] `halopsa/_base_client.py` — Shared request logic, retry, error handling
- [x] `halopsa/_pagination.py` — PageIterator + AsyncPageIterator
- [x] `halopsa/resources/_base.py` — CRUDResource generic base
- [x] `halopsa/client.py` — HaloClient + AsyncHaloClient
- [x] `halopsa/__init__.py` — Public API surface
- [x] `halopsa/_version.py` — Version string
- [x] `halopsa/py.typed` — PEP 561 marker

### Phase 2: Core Models (~33 resources) ✅
- [x] `halopsa/models/ticket.py` — Ticket, TicketList
- [x] `halopsa/models/action.py` — Action, ActionList
- [x] `halopsa/models/client_org.py` — ClientOrg, ClientOrgList
- [x] `halopsa/models/user.py` — User, UserList
- [x] `halopsa/models/agent.py` — Agent, AgentList
- [x] `halopsa/models/asset.py` — Asset, AssetList
- [x] `halopsa/models/site.py` — Site, SiteList
- [x] `halopsa/models/invoice.py` — Invoice
- [x] `halopsa/models/contract.py` — Contract, ContractList
- [x] `halopsa/models/opportunity.py` — Opportunity
- [x] `halopsa/models/project.py` — Project
- [x] `halopsa/models/appointment.py` — Appointment
- [x] `halopsa/models/item.py` — Item
- [x] `halopsa/models/kb_article.py` — KBArticle, KBArticleList
- [x] `halopsa/models/supplier.py` — Supplier, SupplierList
- [x] `halopsa/models/attachment.py` — Attachment
- [x] `halopsa/models/status.py` — Status
- [x] `halopsa/models/team.py` — Team
- [x] `halopsa/models/category.py` — Category
- [x] `halopsa/models/priority.py` — Priority
- [x] `halopsa/models/sla.py` — SLA
- [x] `halopsa/models/ticket_type.py` — TicketType
- [x] `halopsa/models/top_level.py` — TopLevel
- [x] `halopsa/models/expense.py` — Expense
- [x] `halopsa/models/timesheet.py` — Timesheet
- [x] `halopsa/models/release.py` — Release
- [x] `halopsa/models/report.py` — Report
- [x] `halopsa/models/webhook.py` — Webhook
- [x] `halopsa/models/workday.py` — Workday
- [x] `halopsa/models/software_licence.py` — SoftwareLicence
- [x] `halopsa/models/crm_note.py` — CRMNote
- [x] `halopsa/models/quotation.py` — Quotation
- [x] `halopsa/models/__init__.py` — Re-exports

### Phase 3: Core Resources (~33 resource modules) ✅
- [x] `halopsa/resources/tickets.py` — with typed list filters
- [x] `halopsa/resources/actions.py` — with typed list filters
- [x] `halopsa/resources/clients.py`
- [x] `halopsa/resources/users.py` — with `me()` method
- [x] `halopsa/resources/agents.py` — with `me()` method
- [x] `halopsa/resources/assets.py`
- [x] `halopsa/resources/sites.py`
- [x] `halopsa/resources/invoices.py`
- [x] `halopsa/resources/contracts.py`
- [x] `halopsa/resources/opportunities.py`
- [x] `halopsa/resources/projects.py`
- [x] `halopsa/resources/appointments.py`
- [x] `halopsa/resources/items.py`
- [x] `halopsa/resources/kb_articles.py`
- [x] `halopsa/resources/suppliers.py`
- [x] `halopsa/resources/attachments.py` — with S3 presigned URL upload flow
- [x] `halopsa/resources/statuses.py`
- [x] `halopsa/resources/teams.py`
- [x] `halopsa/resources/categories.py`
- [x] `halopsa/resources/priorities.py`
- [x] `halopsa/resources/slas.py`
- [x] `halopsa/resources/ticket_types.py`
- [x] `halopsa/resources/top_levels.py`
- [x] `halopsa/resources/expenses.py` — no DELETE (API doesn't support it)
- [x] `halopsa/resources/timesheets.py` — no DELETE (API doesn't support it)
- [x] `halopsa/resources/releases.py`
- [x] `halopsa/resources/reports.py`
- [x] `halopsa/resources/webhooks.py`
- [x] `halopsa/resources/workdays.py`
- [x] `halopsa/resources/software_licences.py`
- [x] `halopsa/resources/crm_notes.py`
- [x] `halopsa/resources/quotations.py`
- [x] `halopsa/resources/__init__.py`

### Phase 4: CLI ✅
- [x] `halopsa/cli/_config.py` — Config file loading + env var resolution
- [x] `halopsa/cli/_output.py` — Rich table + JSON formatters
- [x] `halopsa/cli/_app.py` — Main Typer app, global options, client factory
- [x] `halopsa/cli/_resource_cmd.py` — DRY resource command factory
- [x] `halopsa/cli/commands/configure.py` — Interactive config setup
- [x] `halopsa/cli/commands/request.py` — Generic API escape hatch
- [x] `halopsa/cli/commands/tickets.py` — Typed filters (18 filter flags)
- [x] `halopsa/cli/commands/actions.py` — Typed filters (ticket_id, agent_id, exclude_sys)
- [x] `halopsa/cli/commands/clients.py` — Typed filters (search, toplevel_id, inactive)
- [x] `halopsa/cli/commands/users.py` — Typed filters + `me` command
- [x] `halopsa/cli/commands/agents.py` — Typed filters + `me` command
- [x] `halopsa/cli/commands/assets.py` — Typed filters (client_id, site_id, assettype_id)
- [x] `halopsa/cli/commands/attachments.py` — Typed filters (ticket_id, action_id)
- [x] `halopsa/cli/commands/sites.py` — Factory CRUD
- [x] `halopsa/cli/commands/invoices.py` — Factory CRUD
- [x] `halopsa/cli/commands/contracts.py` — Factory CRUD
- [x] `halopsa/cli/commands/opportunities.py` — Factory CRUD
- [x] `halopsa/cli/commands/projects.py` — Factory CRUD
- [x] `halopsa/cli/commands/appointments.py` — Factory CRUD
- [x] `halopsa/cli/commands/items.py` — Factory CRUD
- [x] `halopsa/cli/commands/kb_articles.py` — Factory CRUD
- [x] `halopsa/cli/commands/suppliers.py` — Factory CRUD
- [x] `halopsa/cli/commands/statuses.py` — Factory CRUD
- [x] `halopsa/cli/commands/teams.py` — Factory CRUD
- [x] `halopsa/cli/commands/categories.py` — Factory CRUD
- [x] `halopsa/cli/commands/priorities.py` — Factory CRUD
- [x] `halopsa/cli/commands/slas.py` — Factory CRUD
- [x] `halopsa/cli/commands/ticket_types.py` — Factory CRUD
- [x] `halopsa/cli/commands/top_levels.py` — Factory CRUD
- [x] `halopsa/cli/commands/expenses.py` — Factory CRUD (no delete)
- [x] `halopsa/cli/commands/timesheets.py` — Factory CRUD (no delete)
- [x] `halopsa/cli/commands/releases.py` — Factory CRUD
- [x] `halopsa/cli/commands/reports.py` — Factory CRUD
- [x] `halopsa/cli/commands/webhooks.py` — Factory CRUD
- [x] `halopsa/cli/commands/workdays.py` — Factory CRUD
- [x] `halopsa/cli/commands/software_licences.py` — Factory CRUD
- [x] `halopsa/cli/commands/crm_notes.py` — Factory CRUD
- [x] `halopsa/cli/commands/quotations.py` — Factory CRUD
- [x] `halopsa/__main__.py` — `python -m halopsa` entry point
- [x] `pyproject.toml` — Build config, dependencies, `halo` script entry point

### Phase 5: Future
- [ ] Tests
- [ ] More typed filters on remaining resources
- [ ] Typed create/update flags for more resources (currently tickets and actions have them)
- [ ] Shell completion
- [ ] `--output` flag for selecting specific columns

---

## Implemented Typed API Coverage

Legend: `[x]` = implemented in typed resource | `[ ]` = not yet (accessible via `client.request()` or `halo request`)

### Actions (6 endpoints) ⭐ CORE
- [x] GET /Actions
- [x] POST /Actions
- [ ] POST /Actions/Review
- [ ] POST /Actions/reaction
- [x] DELETE /Actions/{id}
- [x] GET /Actions/{id}

### Agent (6 endpoints) ⭐ CORE
- [x] GET /Agent
- [x] POST /Agent
- [ ] POST /Agent/ClearCache
- [x] GET /Agent/me
- [x] DELETE /Agent/{id}
- [x] GET /Agent/{id}

### Appointment (7 endpoints) ⭐ CORE
- [x] GET /Appointment
- [x] POST /Appointment
- [ ] GET /Appointment/Booking
- [ ] POST /Appointment/Booking
- [ ] POST /Appointment/Generate
- [x] DELETE /Appointment/{id}
- [x] GET /Appointment/{id}

### Asset (6 endpoints) ⭐ CORE
- [x] GET /Asset
- [x] POST /Asset
- [ ] GET /Asset/GetAllSoftwareVersions
- [ ] GET /Asset/NextTag
- [x] DELETE /Asset/{id}
- [x] GET /Asset/{id}

### Attachment (14 endpoints) ⭐ CORE
- [x] GET /Attachment
- [x] POST /Attachment
- [x] POST /Attachment/GetS3PresignedURL
- [x] POST /Attachment/PresignedURLUploadComplete
- [ ] POST /Attachment/document
- [ ] DELETE /Attachment/document/{id}
- [ ] GET /Attachment/document/{id}
- [ ] GET /Attachment/image
- [ ] POST /Attachment/image
- [ ] DELETE /Attachment/image/{id}
- [ ] GET /Attachment/image/{id}
- [ ] GET /Attachment/nhserver/{id}
- [x] DELETE /Attachment/{id}
- [x] GET /Attachment/{id}

### CRMNote (4 endpoints) ⭐ CORE
- [x] GET /CRMNote
- [x] POST /CRMNote
- [x] DELETE /CRMNote/{id}
- [x] GET /CRMNote/{id}

### Category (4 endpoints) ⭐ CORE
- [x] GET /Category
- [x] POST /Category
- [x] DELETE /Category/{id}
- [x] GET /Category/{id}

### Client (7 endpoints) ⭐ CORE
- [x] GET /Client
- [x] POST /Client
- [ ] POST /Client/NewAccountsId
- [ ] POST /Client/PaymentMethodUpdate
- [ ] GET /Client/me
- [x] DELETE /Client/{id}
- [x] GET /Client/{id}

### ClientContract (6 endpoints) ⭐ CORE
- [x] GET /ClientContract
- [x] POST /ClientContract
- [ ] POST /ClientContract/Approval
- [ ] POST /ClientContract/NextRef
- [x] DELETE /ClientContract/{id}
- [x] GET /ClientContract/{id}

### Expense (2 endpoints) ⭐ CORE
- [x] GET /Expense
- [x] POST /Expense

### Invoice (9 endpoints) ⭐ CORE
- [x] GET /Invoice
- [x] POST /Invoice
- [ ] POST /Invoice/PDF/{id}
- [ ] POST /Invoice/View
- [ ] GET /Invoice/lines
- [ ] POST /Invoice/updatelines
- [x] DELETE /Invoice/{id}
- [x] GET /Invoice/{id}
- [ ] POST /Invoice/{id}/void

### Item (5 endpoints) ⭐ CORE
- [x] GET /Item
- [x] POST /Item
- [ ] POST /Item/NewAccountsId
- [x] DELETE /Item/{id}
- [x] GET /Item/{id}

### KBArticle (5 endpoints) ⭐ CORE
- [x] GET /KBArticle
- [x] POST /KBArticle
- [ ] POST /KBArticle/vote
- [x] DELETE /KBArticle/{id}
- [x] GET /KBArticle/{id}

### Opportunities (5 endpoints) ⭐ CORE
- [x] GET /Opportunities
- [x] POST /Opportunities
- [ ] POST /Opportunities/View
- [x] DELETE /Opportunities/{id}
- [x] GET /Opportunities/{id}

### Priority (4 endpoints) ⭐ CORE
- [x] GET /Priority
- [x] POST /Priority
- [x] DELETE /Priority/{id}
- [x] GET /Priority/{id}

### Projects (5 endpoints) ⭐ CORE
- [x] GET /Projects
- [x] POST /Projects
- [ ] POST /Projects/View
- [x] DELETE /Projects/{id}
- [x] GET /Projects/{id}

### Quotation (7 endpoints) ⭐ CORE
- [x] GET /Quotation
- [x] POST /Quotation
- [ ] POST /Quotation/Approval
- [ ] POST /Quotation/Lines
- [ ] POST /Quotation/View
- [x] DELETE /Quotation/{id}
- [x] GET /Quotation/{id}

### Release (4 endpoints) ⭐ CORE
- [x] GET /Release
- [x] POST /Release
- [x] DELETE /Release/{id}
- [x] GET /Release/{id}

### Report (7 endpoints) ⭐ CORE
- [x] GET /Report
- [x] POST /Report
- [ ] POST /Report/Bookmark
- [ ] POST /Report/createpdf
- [ ] POST /Report/print
- [x] DELETE /Report/{id}
- [x] GET /Report/{id}

### SLA (4 endpoints) ⭐ CORE
- [x] GET /SLA
- [x] POST /SLA
- [x] DELETE /SLA/{id}
- [x] GET /SLA/{id}

### Site (5 endpoints) ⭐ CORE
- [x] GET /Site
- [x] POST /Site
- [ ] GET /Site/StockBins
- [x] DELETE /Site/{id}
- [x] GET /Site/{id}

### SoftwareLicence (4 endpoints) ⭐ CORE
- [x] GET /SoftwareLicence
- [x] POST /SoftwareLicence
- [x] DELETE /SoftwareLicence/{id}
- [x] GET /SoftwareLicence/{id}

### Status (4 endpoints) ⭐ CORE
- [x] GET /Status
- [x] POST /Status
- [x] DELETE /Status/{id}
- [x] GET /Status/{id}

### Supplier (4 endpoints) ⭐ CORE
- [x] GET /Supplier
- [x] POST /Supplier
- [x] DELETE /Supplier/{id}
- [x] GET /Supplier/{id}

### Team (5 endpoints) ⭐ CORE
- [x] GET /Team
- [x] POST /Team
- [ ] GET /Team/Tree
- [x] DELETE /Team/{id}
- [x] GET /Team/{id}

### TicketType (4 endpoints) ⭐ CORE
- [x] GET /TicketType
- [x] POST /TicketType
- [x] DELETE /TicketType/{id}
- [x] GET /TicketType/{id}

### Tickets (11 endpoints) ⭐ CORE
- [x] GET /Tickets
- [x] POST /Tickets
- [ ] POST /Tickets/Object
- [ ] POST /Tickets/SetBillableProject
- [ ] POST /Tickets/View
- [ ] POST /Tickets/processchildren
- [ ] GET /Tickets/salesmailbox
- [ ] POST /Tickets/vote
- [ ] GET /Tickets/zapier
- [x] DELETE /Tickets/{id}
- [x] GET /Tickets/{id}

### Timesheet (5 endpoints) ⭐ CORE
- [x] GET /Timesheet
- [x] POST /Timesheet
- [ ] GET /Timesheet/forecasting
- [ ] GET /Timesheet/mine
- [x] GET /Timesheet/{id}

### TopLevel (4 endpoints) ⭐ CORE
- [x] GET /TopLevel
- [x] POST /TopLevel
- [x] DELETE /TopLevel/{id}
- [x] GET /TopLevel/{id}

### Users (6 endpoints) ⭐ CORE
- [x] GET /Users
- [x] POST /Users
- [x] GET /Users/me
- [ ] POST /Users/prefs
- [x] DELETE /Users/{id}
- [x] GET /Users/{id}

### Webhook (4 endpoints) ⭐ CORE
- [x] GET /Webhook
- [x] POST /Webhook
- [x] DELETE /Webhook/{id}
- [x] GET /Webhook/{id}

### Workday (4 endpoints) ⭐ CORE
- [x] GET /Workday
- [x] POST /Workday
- [x] DELETE /Workday/{id}
- [x] GET /Workday/{id}

---

**All 1,461 API endpoints (395 resource groups) are accessible via `client.request()` or `halo request`. The above 32 core resources have full typed SDK + CLI support.**
