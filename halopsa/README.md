# HaloPSA Python SDK & CLI

A Python SDK and command-line interface for the [HaloPSA](https://halopsa.com) REST API.

## Installation

Install globally as a CLI tool with [uv](https://docs.astral.sh/uv/):

```bash
uv tool install /path/to/halopsa
```

Make sure `~/.local/bin` is on your PATH:

```bash
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
```

Then `halo` is available everywhere. To reinstall after code changes:

```bash
uv tool install --force /path/to/halopsa
```

Alternatively, install as a library:

```bash
uv pip install .
# or
pip install .
```

This installs both the Python library (`halopsa`) and the `halo` CLI command (accessible via `uv run halo` or after activating the venv).

## Authentication

All API access requires three credentials from your HaloPSA instance:

| Credential | Env var | CLI flag | Config key |
|---|---|---|---|
| Tenant URL | `HALO_TENANT_URL` | `--tenant-url` | `tenant_url` |
| Client ID | `HALO_CLIENT_ID` | `--client-id` | `client_id` |
| Client Secret | `HALO_CLIENT_SECRET` | `--client-secret` | `client_secret` |

Credentials are resolved in order: **CLI flags > environment variables > config file**.

### Config file

Run the interactive setup to save credentials to `~/.halopsa/config.yaml`:

```bash
halo configure
```

The file is created with `0600` permissions. Format:

```yaml
tenant_url: https://company.halopsa.com
client_id: abc123
client_secret: secret456
scope: all
# tenant: mytenant  # optional
```

---

## CLI Usage

```
halo [global-options] <resource> <action> [arguments] [options]
```

### Global options

```
--tenant-url TEXT     HaloPSA tenant URL
--client-id TEXT      OAuth client ID
--client-secret TEXT  OAuth client secret
--json                Output as JSON instead of a table
--no-color            Disable colored output
--version / -v        Show version and exit
```

### Resources

The CLI supports full CRUD (list, get, create, update, delete) for all HaloPSA resources:

tickets, actions, clients, users, agents, assets, sites, invoices, contracts,
opportunities, projects, appointments, items, kb-articles, suppliers,
attachments, statuses, teams, categories, priorities, slas, ticket-types,
top-levels, expenses, timesheets, releases, reports, webhooks, workdays,
software-licences, crm-notes, quotations

### Examples

**List tickets:**

```bash
halo tickets list
halo tickets list --client-id 42 --open-only --search "server"
halo tickets list --all              # fetch every page
halo tickets list --json             # output as JSON
```

**Get a single ticket:**

```bash
halo tickets get 1234
halo tickets get 1234 --json
```

**Create a ticket:**

```bash
halo tickets create --summary "Server down" --client-id 42 --priority-id 1
halo tickets create --summary "Custom" --data '{"details": "extra fields"}'
```

**Update a ticket:**

```bash
halo tickets update 1234 --status-id 5 --agent-id 10
halo tickets update 1234 --data '{"priority_id": 2}'
```

**Delete a ticket:**

```bash
halo tickets delete 1234          # prompts for confirmation
halo tickets delete 1234 --yes    # skip confirmation
```

**Other resources follow the same pattern:**

```bash
halo clients list --search "Acme"
halo agents list --team-id 3
halo agents me
halo users me
halo actions list --ticket-id 1234
halo assets list --client-id 42
halo sites get 5
```

**Generic resources use JSON for create/update:**

```bash
halo teams create --data '{"name": "New Team"}'
halo teams update 7 --data '{"name": "Renamed Team"}'
```

### Raw API requests

For endpoints not covered by a dedicated command, use the escape hatch:

```bash
halo request GET /Tickets --param page_size=5
halo request POST /Tickets --data '{"summary": "Test ticket"}'
halo request DELETE /Tickets/999
```

---

## Python SDK Usage

### Quick start

```python
from halopsa import HaloClient

client = HaloClient(
    tenant_url="https://company.halopsa.com",
    client_id="your-client-id",
    client_secret="your-client-secret",
)

# List tickets
page = client.tickets.list(page_size=10, open_only=True)
for ticket in page.items:
    print(ticket.id, ticket.summary)

# Get a single ticket
ticket = client.tickets.get(1234)
print(ticket.summary, ticket.status_name)

# Create a ticket
new = client.tickets.create({"summary": "Server down", "client_id": 42})
print(f"Created ticket #{new.id}")

# Update a ticket
updated = client.tickets.update({"id": 1234, "status_id": 5})

# Delete a ticket
client.tickets.delete(1234)
```

### Pagination

```python
# Single page
page = client.tickets.list(page_size=50, page_no=1)
print(f"{page.record_count} total tickets")

# Auto-paginate through all results
for ticket in client.tickets.list_all(page_size=100):
    print(ticket.id, ticket.summary)
```

### Async client

```python
import asyncio
from halopsa import AsyncHaloClient

async def main():
    client = AsyncHaloClient(
        tenant_url="https://company.halopsa.com",
        client_id="your-client-id",
        client_secret="your-client-secret",
    )
    page = await client.tickets.alist(open_only=True)
    for ticket in page.items:
        print(ticket.summary)
    await client.close()

asyncio.run(main())
```

### Context manager

```python
with HaloClient(
    tenant_url="https://company.halopsa.com",
    client_id="your-client-id",
    client_secret="your-client-secret",
) as client:
    agents = client.agents.list()
    me = client.agents.me()
```

### Available resources

All resources are accessible as attributes on the client:

| Attribute | Resource |
|---|---|
| `client.tickets` | Tickets |
| `client.actions` | Actions |
| `client.clients` | Client organisations |
| `client.users` | Users |
| `client.agents` | Agents |
| `client.assets` | Assets |
| `client.sites` | Sites |
| `client.invoices` | Invoices |
| `client.contracts` | Contracts |
| `client.opportunities` | Opportunities |
| `client.projects` | Projects |
| `client.appointments` | Appointments |
| `client.items` | Items |
| `client.kb_articles` | Knowledge base articles |
| `client.suppliers` | Suppliers |
| `client.attachments` | Attachments |
| `client.statuses` | Statuses |
| `client.teams` | Teams |
| `client.categories` | Categories |
| `client.priorities` | Priorities |
| `client.slas` | SLAs |
| `client.ticket_types` | Ticket types |
| `client.top_levels` | Top levels |
| `client.expenses` | Expenses |
| `client.timesheets` | Timesheets |
| `client.releases` | Releases |
| `client.reports` | Reports |
| `client.webhooks` | Webhooks |
| `client.workdays` | Workdays |
| `client.software_licences` | Software licences |
| `client.crm_notes` | CRM notes |
| `client.quotations` | Quotations |

Each resource supports: `list()`, `list_all()`, `get(id)`, `create(data)`, `update(data)`, `delete(id)`, and `batch_create(items)`.

### Error handling

```python
from halopsa import HaloNotFoundError, HaloAuthenticationError

try:
    ticket = client.tickets.get(99999)
except HaloNotFoundError:
    print("Ticket not found")
except HaloAuthenticationError:
    print("Invalid credentials")
```

Exception hierarchy:

- `HaloError` — base
  - `HaloAPIError` — any API error (has `status_code` and `body`)
    - `HaloValidationError` (400)
    - `HaloAuthenticationError` (401)
    - `HaloForbiddenError` (403)
    - `HaloNotFoundError` (404)
    - `HaloRateLimitError` (429)
    - `HaloServerError` (5xx)
  - `HaloTokenError` — OAuth token failure
  - `HaloTimeoutError` — request timeout
