# HaloPSA Python Library — Progress Tracker

**Total: 395 resource groups | 1,461 operations | 0 implemented**

---

## Implementation Phases

### Phase 1: Foundation
- [ ] `halopsa/exceptions.py` — Exception hierarchy
- [ ] `halopsa/models/_base.py` — HaloModel base + PaginatedResponse
- [ ] `halopsa/models/_common.py` — CustomField + shared types
- [ ] `halopsa/auth.py` — TokenManager (OAuth2 client_credentials)
- [ ] `halopsa/_transport.py` — _SyncTransport + _AsyncTransport
- [ ] `halopsa/_base_client.py` — Shared request logic, retry, error handling
- [ ] `halopsa/_pagination.py` — PageIterator + AsyncPageIterator
- [ ] `halopsa/resources/_base.py` — CRUDResource generic base
- [ ] `halopsa/client.py` — HaloClient + AsyncHaloClient
- [ ] `halopsa/__init__.py` — Public API surface
- [ ] `halopsa/_version.py` — Version string
- [ ] `halopsa/py.typed` — PEP 561 marker

### Phase 2: Core Models (~33 resources)
- [ ] `halopsa/models/ticket.py` — Ticket, TicketList
- [ ] `halopsa/models/action.py` — Action, ActionList
- [ ] `halopsa/models/client_org.py` — ClientOrg, ClientOrgList
- [ ] `halopsa/models/user.py` — User, UserList
- [ ] `halopsa/models/agent.py` — Agent, AgentList
- [ ] `halopsa/models/asset.py` — Asset, AssetList
- [ ] `halopsa/models/site.py` — Site, SiteList
- [ ] `halopsa/models/invoice.py` — Invoice
- [ ] `halopsa/models/contract.py` — Contract, ContractList
- [ ] `halopsa/models/opportunity.py` — Opportunity
- [ ] `halopsa/models/project.py` — Project
- [ ] `halopsa/models/appointment.py` — Appointment
- [ ] `halopsa/models/item.py` — Item
- [ ] `halopsa/models/kb_article.py` — KBArticle, KBArticleList
- [ ] `halopsa/models/supplier.py` — Supplier, SupplierList
- [ ] `halopsa/models/attachment.py` — Attachment
- [ ] `halopsa/models/status.py` — Status
- [ ] `halopsa/models/team.py` — Team
- [ ] `halopsa/models/category.py` — Category
- [ ] `halopsa/models/priority.py` — Priority
- [ ] `halopsa/models/sla.py` — SLA
- [ ] `halopsa/models/ticket_type.py` — TicketType
- [ ] `halopsa/models/top_level.py` — TopLevel
- [ ] `halopsa/models/expense.py` — Expense
- [ ] `halopsa/models/timesheet.py` — Timesheet
- [ ] `halopsa/models/release.py` — Release
- [ ] `halopsa/models/report.py` — Report
- [ ] `halopsa/models/webhook.py` — Webhook
- [ ] `halopsa/models/workday.py` — Workday
- [ ] `halopsa/models/software_licence.py` — SoftwareLicence
- [ ] `halopsa/models/crm_note.py` — CRMNote
- [ ] `halopsa/models/quotation.py` — Quotation
- [ ] `halopsa/models/__init__.py` — Re-exports

### Phase 3: Core Resources (~33 resource modules)
- [ ] `halopsa/resources/tickets.py`
- [ ] `halopsa/resources/actions.py`
- [ ] `halopsa/resources/clients.py`
- [ ] `halopsa/resources/users.py`
- [ ] `halopsa/resources/agents.py`
- [ ] `halopsa/resources/assets.py`
- [ ] `halopsa/resources/sites.py`
- [ ] `halopsa/resources/invoices.py`
- [ ] `halopsa/resources/contracts.py`
- [ ] `halopsa/resources/opportunities.py`
- [ ] `halopsa/resources/projects.py`
- [ ] `halopsa/resources/appointments.py`
- [ ] `halopsa/resources/items.py`
- [ ] `halopsa/resources/kb_articles.py`
- [ ] `halopsa/resources/suppliers.py`
- [ ] `halopsa/resources/attachments.py`
- [ ] `halopsa/resources/statuses.py`
- [ ] `halopsa/resources/teams.py`
- [ ] `halopsa/resources/categories.py`
- [ ] `halopsa/resources/priorities.py`
- [ ] `halopsa/resources/slas.py`
- [ ] `halopsa/resources/ticket_types.py`
- [ ] `halopsa/resources/top_levels.py`
- [ ] `halopsa/resources/expenses.py`
- [ ] `halopsa/resources/timesheets.py`
- [ ] `halopsa/resources/releases.py`
- [ ] `halopsa/resources/reports.py`
- [ ] `halopsa/resources/webhooks.py`
- [ ] `halopsa/resources/workdays.py`
- [ ] `halopsa/resources/software_licences.py`
- [ ] `halopsa/resources/crm_notes.py`
- [ ] `halopsa/resources/quotations.py`
- [ ] `halopsa/resources/__init__.py`

### Phase 4: Special Features
- [ ] S3 presigned URL upload flow in attachments
- [ ] Code generation scripts for remaining endpoints

---

## All 1,461 API Endpoints (395 resource groups)

Legend: `[x]` = implemented in typed resource | `[ ]` = not yet implemented (accessible via `client.request()`)

### AISuggestion (4 endpoints)
- [ ] GET /AISuggestion
- [ ] POST /AISuggestion
- [ ] DELETE /AISuggestion/{id}
- [ ] GET /AISuggestion/{id}

### ATT (1 endpoints)
- [ ] GET /ATT/PriceAndAvailability

### AWS (1 endpoints)
- [ ] GET /AWS/Get

### AWSDetails (4 endpoints)
- [ ] GET /AWSDetails
- [ ] POST /AWSDetails
- [ ] DELETE /AWSDetails/{id}
- [ ] GET /AWSDetails/{id}

### Actions (6 endpoints) ⭐ CORE
- [ ] GET /Actions
- [ ] POST /Actions
- [ ] POST /Actions/Review
- [ ] POST /Actions/reaction
- [ ] DELETE /Actions/{id}
- [ ] GET /Actions/{id}

### Addigy (2 endpoints)
- [ ] GET /Addigy/Get
- [ ] POST /Addigy/Post

### AddigyDetails (4 endpoints)
- [ ] GET /AddigyDetails
- [ ] POST /AddigyDetails
- [ ] DELETE /AddigyDetails/{id}
- [ ] GET /AddigyDetails/{id}

### Address (4 endpoints)
- [ ] GET /Address
- [ ] POST /Address
- [ ] DELETE /Address/{id}
- [ ] GET /Address/{id}

### Addressbook (4 endpoints)
- [ ] GET /Addressbook
- [ ] POST /Addressbook
- [ ] DELETE /Addressbook/{id}
- [ ] GET /Addressbook/{id}

### AdobeAcrobatDetails (4 endpoints)
- [ ] GET /AdobeAcrobatDetails
- [ ] POST /AdobeAcrobatDetails
- [ ] DELETE /AdobeAcrobatDetails/{id}
- [ ] GET /AdobeAcrobatDetails/{id}

### AdobeCommerceDetails (4 endpoints)
- [ ] GET /AdobeCommerceDetails
- [ ] POST /AdobeCommerceDetails
- [ ] DELETE /AdobeCommerceDetails/{id}
- [ ] GET /AdobeCommerceDetails/{id}

### AdobeCommerceIntegration (2 endpoints)
- [ ] GET /AdobeCommerceIntegration
- [ ] POST /AdobeCommerceIntegration/auth

### Agent (6 endpoints) ⭐ CORE
- [ ] GET /Agent
- [ ] POST /Agent
- [ ] POST /Agent/ClearCache
- [ ] GET /Agent/me
- [ ] DELETE /Agent/{id}
- [ ] GET /Agent/{id}

### AgentCheckIn (3 endpoints)
- [ ] GET /AgentCheckIn
- [ ] POST /AgentCheckIn
- [ ] GET /AgentCheckIn/{id}

### AgentEventSubscription (4 endpoints)
- [ ] GET /AgentEventSubscription
- [ ] POST /AgentEventSubscription
- [ ] DELETE /AgentEventSubscription/{id}
- [ ] GET /AgentEventSubscription/{id}

### AgentImage (1 endpoints)
- [ ] GET /AgentImage/{id}

### AgentPresenceRule (1 endpoints)
- [ ] GET /AgentPresenceRule

### AgentPresenceSubscription (4 endpoints)
- [ ] GET /AgentPresenceSubscription
- [ ] POST /AgentPresenceSubscription
- [ ] DELETE /AgentPresenceSubscription/{id}
- [ ] GET /AgentPresenceSubscription/{id}

### Alemba (1 endpoints)
- [ ] GET /Alemba/Get

### AmazonSellerDetails (4 endpoints)
- [ ] GET /AmazonSellerDetails
- [ ] POST /AmazonSellerDetails
- [ ] DELETE /AmazonSellerDetails/{id}
- [ ] GET /AmazonSellerDetails/{id}

### Application (5 endpoints)
- [ ] GET /Application
- [ ] POST /Application
- [ ] POST /Application/federatedcredentials
- [ ] DELETE /Application/{id}
- [ ] GET /Application/{id}

### Appointment (7 endpoints) ⭐ CORE
- [ ] GET /Appointment
- [ ] POST /Appointment
- [ ] GET /Appointment/Booking
- [ ] POST /Appointment/Booking
- [ ] POST /Appointment/Generate
- [ ] DELETE /Appointment/{id}
- [ ] GET /Appointment/{id}

### ApprovalProcess (4 endpoints)
- [ ] GET /ApprovalProcess
- [ ] POST /ApprovalProcess
- [ ] DELETE /ApprovalProcess/{id}
- [ ] GET /ApprovalProcess/{id}

### ApprovalProcessRule (4 endpoints)
- [ ] GET /ApprovalProcessRule
- [ ] POST /ApprovalProcessRule
- [ ] DELETE /ApprovalProcessRule/{id}
- [ ] GET /ApprovalProcessRule/{id}

### ApprovalStore (1 endpoints)
- [ ] POST /ApprovalStore

### AreaAzureTenant (1 endpoints)
- [ ] GET /AreaAzureTenant

### AreaRequestType (2 endpoints)
- [ ] GET /AreaRequestType
- [ ] GET /AreaRequestType/{id}

### Armis (1 endpoints)
- [ ] GET /Armis/Get

### ArmisDetails (4 endpoints)
- [ ] GET /ArmisDetails
- [ ] POST /ArmisDetails
- [ ] DELETE /ArmisDetails/{id}
- [ ] GET /ArmisDetails/{id}

### ArrowSphereDetails (4 endpoints)
- [ ] GET /ArrowSphereDetails
- [ ] POST /ArrowSphereDetails
- [ ] DELETE /ArrowSphereDetails/{id}
- [ ] GET /ArrowSphereDetails/{id}

### Asset (6 endpoints) ⭐ CORE
- [ ] GET /Asset
- [ ] POST /Asset
- [ ] GET /Asset/GetAllSoftwareVersions
- [ ] GET /Asset/NextTag
- [ ] DELETE /Asset/{id}
- [ ] GET /Asset/{id}

### AssetChange (2 endpoints)
- [ ] GET /AssetChange
- [ ] POST /AssetChange

### AssetGroup (4 endpoints)
- [ ] GET /AssetGroup
- [ ] POST /AssetGroup
- [ ] DELETE /AssetGroup/{id}
- [ ] GET /AssetGroup/{id}

### AssetSoftware (1 endpoints)
- [ ] GET /AssetSoftware

### AssetType (4 endpoints)
- [ ] GET /AssetType
- [ ] POST /AssetType
- [ ] DELETE /AssetType/{id}
- [ ] GET /AssetType/{id}

### AssetTypeInfo (1 endpoints)
- [ ] GET /AssetTypeInfo

### AssetTypeMappings (2 endpoints)
- [ ] GET /AssetTypeMappings
- [ ] GET /AssetTypeMappings/{id}

### Attachment (14 endpoints) ⭐ CORE
- [ ] GET /Attachment
- [ ] POST /Attachment
- [ ] POST /Attachment/GetS3PresignedURL
- [ ] POST /Attachment/PresignedURLUploadComplete
- [ ] POST /Attachment/document
- [ ] DELETE /Attachment/document/{id}
- [ ] GET /Attachment/document/{id}
- [ ] GET /Attachment/image
- [ ] POST /Attachment/image
- [ ] DELETE /Attachment/image/{id}
- [ ] GET /Attachment/image/{id}
- [ ] GET /Attachment/nhserver/{id}
- [ ] DELETE /Attachment/{id}
- [ ] GET /Attachment/{id}

### Audit (4 endpoints)
- [ ] GET /Audit
- [ ] POST /Audit
- [ ] DELETE /Audit/{id}
- [ ] GET /Audit/{id}

### AuthInfo (1 endpoints)
- [ ] GET /AuthInfo

### Automation (5 endpoints)
- [ ] GET /Automation
- [ ] POST /Automation
- [ ] DELETE /Automation/{id}
- [ ] GET /Automation/{id}
- [ ] POST /Automation/{runbookId}

### AvalaraDetails (4 endpoints)
- [ ] GET /AvalaraDetails
- [ ] POST /AvalaraDetails
- [ ] DELETE /AvalaraDetails/{id}
- [ ] GET /AvalaraDetails/{id}

### AzureDelta (4 endpoints)
- [ ] GET /AzureDelta
- [ ] POST /AzureDelta
- [ ] DELETE /AzureDelta/{id}
- [ ] GET /AzureDelta/{id}

### AzureDevOpsDetails (4 endpoints)
- [ ] GET /AzureDevOpsDetails
- [ ] POST /AzureDevOpsDetails
- [ ] DELETE /AzureDevOpsDetails/{id}
- [ ] GET /AzureDevOpsDetails/{id}

### AzureTranslate (2 endpoints)
- [ ] GET /AzureTranslate/CustomTranslate
- [ ] POST /AzureTranslate/LanguagePackTranslate

### BackgroundTask (1 endpoints)
- [ ] GET /BackgroundTask/{id}

### BillingTemplate (4 endpoints)
- [ ] GET /BillingTemplate
- [ ] POST /BillingTemplate
- [ ] DELETE /BillingTemplate/{id}
- [ ] GET /BillingTemplate/{id}

### BookingType (1 endpoints)
- [ ] GET /BookingType

### Bookmark (2 endpoints)
- [ ] POST /Bookmark
- [ ] GET /Bookmark/{id}

### BudgetType (4 endpoints)
- [ ] GET /BudgetType
- [ ] POST /BudgetType
- [ ] DELETE /BudgetType/{id}
- [ ] GET /BudgetType/{id}

### BulkEmail (2 endpoints)
- [ ] GET /BulkEmail
- [ ] GET /BulkEmail/{id}

### BusinessCentralDetails (4 endpoints)
- [ ] GET /BusinessCentralDetails
- [ ] POST /BusinessCentralDetails
- [ ] DELETE /BusinessCentralDetails/{id}
- [ ] GET /BusinessCentralDetails/{id}

### CAB (4 endpoints)
- [ ] GET /CAB
- [ ] POST /CAB
- [ ] DELETE /CAB/{id}
- [ ] GET /CAB/{id}

### CABMember (1 endpoints)
- [ ] GET /CABMember

### CABRole (1 endpoints)
- [ ] GET /CABRole

### CRMNote (4 endpoints) ⭐ CORE
- [ ] GET /CRMNote
- [ ] POST /CRMNote
- [ ] DELETE /CRMNote/{id}
- [ ] GET /CRMNote/{id}

### CSPConsumptionData (6 endpoints)
- [ ] GET /CSPConsumptionData
- [ ] POST /CSPConsumptionData
- [ ] DELETE /CSPConsumptionData/Parent/{id}
- [ ] POST /CSPConsumptionData/manage
- [ ] DELETE /CSPConsumptionData/{id}
- [ ] GET /CSPConsumptionData/{id}

### CSPSubscriptionPricing (1 endpoints)
- [ ] POST /CSPSubscriptionPricing/manage

### CSVTemplate (4 endpoints)
- [ ] GET /CSVTemplate
- [ ] POST /CSVTemplate
- [ ] DELETE /CSVTemplate/{id}
- [ ] GET /CSVTemplate/{id}

### CallLog (3 endpoints)
- [ ] GET /CallLog
- [ ] POST /CallLog
- [ ] GET /CallLog/{id}

### CallScript (4 endpoints)
- [ ] GET /CallScript
- [ ] POST /CallScript
- [ ] DELETE /CallScript/{id}
- [ ] GET /CallScript/{id}

### CannedText (5 endpoints)
- [ ] GET /CannedText
- [ ] POST /CannedText
- [ ] POST /CannedText/favourite
- [ ] DELETE /CannedText/{id}
- [ ] GET /CannedText/{id}

### Category (4 endpoints) ⭐ CORE
- [ ] GET /Category
- [ ] POST /Category
- [ ] DELETE /Category/{id}
- [ ] GET /Category/{id}

### Certificate (4 endpoints)
- [ ] GET /Certificate
- [ ] POST /Certificate
- [ ] DELETE /Certificate/{id}
- [ ] GET /Certificate/{id}

### ChangeCalendar (1 endpoints)
- [ ] GET /ChangeCalendar

### ChargeRate (2 endpoints)
- [ ] GET /ChargeRate
- [ ] GET /ChargeRate/{id}

### Chat (3 endpoints)
- [ ] GET /Chat
- [ ] POST /Chat
- [ ] GET /Chat/{id}

### ChatFlow (1 endpoints)
- [ ] POST /ChatFlow

### ChatMatchingData (1 endpoints)
- [ ] POST /ChatMatchingData

### ChatMessage (3 endpoints)
- [ ] GET /ChatMessage
- [ ] POST /ChatMessage
- [ ] POST /ChatMessage/IsTyping

### ChatProfile (4 endpoints)
- [ ] GET /ChatProfile
- [ ] POST /ChatProfile
- [ ] DELETE /ChatProfile/{id}
- [ ] GET /ChatProfile/{id}

### Client (7 endpoints) ⭐ CORE
- [ ] GET /Client
- [ ] POST /Client
- [ ] POST /Client/NewAccountsId
- [ ] POST /Client/PaymentMethodUpdate
- [ ] GET /Client/me
- [ ] DELETE /Client/{id}
- [ ] GET /Client/{id}

### ClientCache (1 endpoints)
- [ ] GET /ClientCache

### ClientContract (6 endpoints) ⭐ CORE
- [ ] GET /ClientContract
- [ ] POST /ClientContract
- [ ] POST /ClientContract/Approval
- [ ] POST /ClientContract/NextRef
- [ ] DELETE /ClientContract/{id}
- [ ] GET /ClientContract/{id}

### ClientPrepay (4 endpoints)
- [ ] GET /ClientPrepay
- [ ] POST /ClientPrepay
- [ ] DELETE /ClientPrepay/{id}
- [ ] GET /ClientPrepay/{id}

### ConfigCommit (4 endpoints)
- [ ] GET /ConfigCommit
- [ ] POST /ConfigCommit
- [ ] DELETE /ConfigCommit/{id}
- [ ] GET /ConfigCommit/{id}

### ConfirmClosure (4 endpoints)
- [ ] GET /ConfirmClosure
- [ ] POST /ConfirmClosure
- [ ] DELETE /ConfirmClosure/{id}
- [ ] GET /ConfirmClosure/{id}

### ConfluenceDetails (4 endpoints)
- [ ] GET /ConfluenceDetails
- [ ] POST /ConfluenceDetails
- [ ] DELETE /ConfluenceDetails/{id}
- [ ] GET /ConfluenceDetails/{id}

### ConnectedInstance (4 endpoints)
- [ ] GET /ConnectedInstance
- [ ] POST /ConnectedInstance
- [ ] DELETE /ConnectedInstance/{id}
- [ ] GET /ConnectedInstance/{id}

### Consignment (4 endpoints)
- [ ] GET /Consignment
- [ ] POST /Consignment
- [ ] DELETE /Consignment/{id}
- [ ] GET /Consignment/{id}

### Contactgroup (4 endpoints)
- [ ] GET /Contactgroup
- [ ] POST /Contactgroup
- [ ] DELETE /Contactgroup/{id}
- [ ] GET /Contactgroup/{id}

### Contactgroupcontact (4 endpoints)
- [ ] GET /Contactgroupcontact
- [ ] POST /Contactgroupcontact
- [ ] DELETE /Contactgroupcontact/{id}
- [ ] GET /Contactgroupcontact/{id}

### ContractRule (4 endpoints)
- [ ] GET /ContractRule
- [ ] POST /ContractRule
- [ ] DELETE /ContractRule/{id}
- [ ] GET /ContractRule/{id}

### ContractSchedule (4 endpoints)
- [ ] GET /ContractSchedule
- [ ] POST /ContractSchedule
- [ ] DELETE /ContractSchedule/{id}
- [ ] GET /ContractSchedule/{id}

### ContractSchedulePlan (4 endpoints)
- [ ] GET /ContractSchedulePlan
- [ ] POST /ContractSchedulePlan
- [ ] DELETE /ContractSchedulePlan/{id}
- [ ] GET /ContractSchedulePlan/{id}

### Control (6 endpoints)
- [ ] GET /Control
- [ ] POST /Control
- [ ] POST /Control/ClearCache
- [ ] GET /Control/Teams
- [ ] POST /Control/UpdateEnc
- [ ] POST /Control/setup

### CostCentres (4 endpoints)
- [ ] GET /CostCentres
- [ ] POST /CostCentres
- [ ] DELETE /CostCentres/{id}
- [ ] GET /CostCentres/{id}

### CriteriaGroup (1 endpoints)
- [ ] GET /CriteriaGroup

### Currency (4 endpoints)
- [ ] GET /Currency
- [ ] POST /Currency
- [ ] DELETE /Currency/{id}
- [ ] GET /Currency/{id}

### CustomButton (4 endpoints)
- [ ] GET /CustomButton
- [ ] POST /CustomButton
- [ ] DELETE /CustomButton/{id}
- [ ] GET /CustomButton/{id}

### CustomButtonAudit (1 endpoints)
- [ ] POST /CustomButtonAudit

### CustomIntegration (4 endpoints)
- [ ] GET /CustomIntegration
- [ ] POST /CustomIntegration
- [ ] DELETE /CustomIntegration/{id}
- [ ] GET /CustomIntegration/{id}

### CustomIntegrationMethod (4 endpoints)
- [ ] GET /CustomIntegrationMethod
- [ ] POST /CustomIntegrationMethod
- [ ] DELETE /CustomIntegrationMethod/{id}
- [ ] GET /CustomIntegrationMethod/{id}

### CustomIntegrationMethodValue (1 endpoints)
- [ ] GET /CustomIntegrationMethodValue

### CustomIntegrationRepository (2 endpoints)
- [ ] GET /CustomIntegrationRepository
- [ ] GET /CustomIntegrationRepository/{id}

### CustomQuery (4 endpoints)
- [ ] GET /CustomQuery
- [ ] POST /CustomQuery
- [ ] DELETE /CustomQuery/{id}
- [ ] GET /CustomQuery/{id}

### CustomTable (4 endpoints)
- [ ] GET /CustomTable
- [ ] POST /CustomTable
- [ ] DELETE /CustomTable/{id}
- [ ] GET /CustomTable/{id}

### DashboardLinks (5 endpoints)
- [ ] GET /DashboardLinks
- [ ] POST /DashboardLinks
- [ ] GET /DashboardLinks/FilterValues
- [ ] DELETE /DashboardLinks/{id}
- [ ] GET /DashboardLinks/{id}

### DashboardLinksRepository (2 endpoints)
- [ ] GET /DashboardLinksRepository
- [ ] GET /DashboardLinksRepository/{id}

### DatabaseLookup (5 endpoints)
- [ ] GET /DatabaseLookup
- [ ] POST /DatabaseLookup
- [ ] POST /DatabaseLookup/run
- [ ] DELETE /DatabaseLookup/{id}
- [ ] GET /DatabaseLookup/{id}

### DatabaseLookupConfirmation (2 endpoints)
- [ ] POST /DatabaseLookupConfirmation
- [ ] GET /DatabaseLookupConfirmation/{id}

### DattoCommerceDetails (4 endpoints)
- [ ] GET /DattoCommerceDetails
- [ ] POST /DattoCommerceDetails
- [ ] DELETE /DattoCommerceDetails/{id}
- [ ] GET /DattoCommerceDetails/{id}

### DattoRmmDetails (4 endpoints)
- [ ] GET /DattoRmmDetails
- [ ] POST /DattoRmmDetails
- [ ] DELETE /DattoRmmDetails/{id}
- [ ] GET /DattoRmmDetails/{id}

### DeviceLicence (1 endpoints)
- [ ] GET /DeviceLicence

### DistributionLists (4 endpoints)
- [ ] GET /DistributionLists
- [ ] POST /DistributionLists
- [ ] DELETE /DistributionLists/{id}
- [ ] GET /DistributionLists/{id}

### DistributionListsLog (4 endpoints)
- [ ] GET /DistributionListsLog
- [ ] POST /DistributionListsLog
- [ ] DELETE /DistributionListsLog/{id}
- [ ] GET /DistributionListsLog/{id}

### DocumentCreation (1 endpoints)
- [ ] POST /DocumentCreation

### Downtime (5 endpoints)
- [ ] GET /Downtime
- [ ] POST /Downtime
- [ ] GET /Downtime/DowntimeCalendar
- [ ] DELETE /Downtime/{id}
- [ ] GET /Downtime/{id}

### Draft (1 endpoints)
- [ ] POST /Draft

### Dynamics365CRMDetails (4 endpoints)
- [ ] GET /Dynamics365CRMDetails
- [ ] POST /Dynamics365CRMDetails
- [ ] DELETE /Dynamics365CRMDetails/{id}
- [ ] GET /Dynamics365CRMDetails/{id}

### DynatraceDetails (4 endpoints)
- [ ] GET /DynatraceDetails
- [ ] POST /DynatraceDetails
- [ ] DELETE /DynatraceDetails/{id}
- [ ] GET /DynatraceDetails/{id}

### EcommerceOrder (4 endpoints)
- [ ] GET /EcommerceOrder
- [ ] POST /EcommerceOrder
- [ ] DELETE /EcommerceOrder/{id}
- [ ] GET /EcommerceOrder/{id}

### EmailAddressBook (1 endpoints)
- [ ] GET /EmailAddressBook

### EmailRule (4 endpoints)
- [ ] GET /EmailRule
- [ ] POST /EmailRule
- [ ] DELETE /EmailRule/{id}
- [ ] GET /EmailRule/{id}

### EmailStore (4 endpoints)
- [ ] GET /EmailStore
- [ ] POST /EmailStore
- [ ] DELETE /EmailStore/{id}
- [ ] GET /EmailStore/{id}

### EmailTemplate (5 endpoints)
- [ ] GET /EmailTemplate
- [ ] POST /EmailTemplate
- [ ] POST /EmailTemplate/preview
- [ ] DELETE /EmailTemplate/{id}
- [ ] GET /EmailTemplate/{id}

### EmailTemplateVariable (4 endpoints)
- [ ] GET /EmailTemplateVariable
- [ ] POST /EmailTemplateVariable
- [ ] DELETE /EmailTemplateVariable/{id}
- [ ] GET /EmailTemplateVariable/{id}

### Eracent (1 endpoints)
- [ ] GET /Eracent/Get

### EracentDetails (4 endpoints)
- [ ] GET /EracentDetails
- [ ] POST /EracentDetails
- [ ] DELETE /EracentDetails/{id}
- [ ] GET /EracentDetails/{id}

### Event (4 endpoints)
- [ ] GET /Event
- [ ] POST /Event
- [ ] DELETE /Event/{id}
- [ ] GET /Event/{id}

### EventRule (4 endpoints)
- [ ] GET /EventRule
- [ ] POST /EventRule
- [ ] DELETE /EventRule/{id}
- [ ] GET /EventRule/{id}

### ExactDetails (4 endpoints)
- [ ] GET /ExactDetails
- [ ] POST /ExactDetails
- [ ] DELETE /ExactDetails/{id}
- [ ] GET /ExactDetails/{id}

### Example (1 endpoints)
- [ ] GET /Example/Get

### Expense (2 endpoints) ⭐ CORE
- [ ] GET /Expense
- [ ] POST /Expense

### ExternalChatMessage (4 endpoints)
- [ ] GET /ExternalChatMessage
- [ ] POST /ExternalChatMessage
- [ ] DELETE /ExternalChatMessage/{id}
- [ ] GET /ExternalChatMessage/{id}

### ExternalLink (5 endpoints)
- [ ] GET /ExternalLink
- [ ] POST /ExternalLink
- [ ] POST /ExternalLink/Generate
- [ ] DELETE /ExternalLink/{id}
- [ ] GET /ExternalLink/{id}

### FAQLists (4 endpoints)
- [ ] GET /FAQLists
- [ ] POST /FAQLists
- [ ] DELETE /FAQLists/{id}
- [ ] GET /FAQLists/{id}

### FacebookDetails (4 endpoints)
- [ ] GET /FacebookDetails
- [ ] POST /FacebookDetails
- [ ] DELETE /FacebookDetails/{id}
- [ ] GET /FacebookDetails/{id}

### FaultViewLog (1 endpoints)
- [ ] GET /FaultViewLog

### FaultsForecasting (2 endpoints)
- [ ] POST /FaultsForecasting
- [ ] GET /FaultsForecasting/{id}

### Features (3 endpoints)
- [ ] GET /Features
- [ ] POST /Features
- [ ] GET /Features/{id}

### Feed (1 endpoints)
- [ ] GET /Feed

### Feedback (5 endpoints)
- [ ] GET /Feedback
- [ ] POST /Feedback
- [ ] GET /Feedback/FeedbackMessage
- [ ] DELETE /Feedback/{id}
- [ ] GET /Feedback/{id}

### Field (5 endpoints)
- [ ] GET /Field
- [ ] POST /Field
- [ ] POST /Field/AddFieldToAll/{id}
- [ ] DELETE /Field/{id}
- [ ] GET /Field/{id}

### FieldGroup (4 endpoints)
- [ ] GET /FieldGroup
- [ ] POST /FieldGroup
- [ ] DELETE /FieldGroup/{id}
- [ ] GET /FieldGroup/{id}

### FieldInfo (4 endpoints)
- [ ] GET /FieldInfo
- [ ] POST /FieldInfo
- [ ] DELETE /FieldInfo/{id}
- [ ] GET /FieldInfo/{id}

### ForecastDetails (4 endpoints)
- [ ] GET /ForecastDetails
- [ ] POST /ForecastDetails
- [ ] DELETE /ForecastDetails/{id}
- [ ] GET /ForecastDetails/{id}

### ForethoughtDetails (4 endpoints)
- [ ] GET /ForethoughtDetails
- [ ] POST /ForethoughtDetails
- [ ] DELETE /ForethoughtDetails/{id}
- [ ] GET /ForethoughtDetails/{id}

### FortnoxDetails (4 endpoints)
- [ ] GET /FortnoxDetails
- [ ] POST /FortnoxDetails
- [ ] DELETE /FortnoxDetails/{id}
- [ ] GET /FortnoxDetails/{id}

### GWorkspaceDetails (4 endpoints)
- [ ] GET /GWorkspaceDetails
- [ ] POST /GWorkspaceDetails
- [ ] DELETE /GWorkspaceDetails/{id}
- [ ] GET /GWorkspaceDetails/{id}

### GoToResolve (2 endpoints)
- [ ] GET /GoToResolve/Complete
- [ ] GET /GoToResolve/Download

### GoogleBusinessDetails (4 endpoints)
- [ ] GET /GoogleBusinessDetails
- [ ] POST /GoogleBusinessDetails
- [ ] DELETE /GoogleBusinessDetails/{id}
- [ ] GET /GoogleBusinessDetails/{id}

### HaloDeviceInfo (3 endpoints)
- [ ] POST /HaloDeviceInfo
- [ ] DELETE /HaloDeviceInfo/{id}
- [ ] GET /HaloDeviceInfo/{id}

### HaloField (1 endpoints)
- [ ] GET /HaloField

### HaloIntegration (3 endpoints)
- [ ] POST /HaloIntegration/CreateAction
- [ ] POST /HaloIntegration/CreateTicket
- [ ] GET /HaloIntegration/Get

### HaloNews (5 endpoints)
- [ ] GET /HaloNews
- [ ] POST /HaloNews
- [ ] POST /HaloNews/read
- [ ] DELETE /HaloNews/{id}
- [ ] GET /HaloNews/{id}

### Health (2 endpoints)
- [ ] GET /Health
- [ ] GET /Health/Hashing

### HistoricalTicketVolumes (4 endpoints)
- [ ] GET /HistoricalTicketVolumes
- [ ] POST /HistoricalTicketVolumes
- [ ] DELETE /HistoricalTicketVolumes/{id}
- [ ] GET /HistoricalTicketVolumes/{id}

### Holiday (4 endpoints)
- [ ] GET /Holiday
- [ ] POST /Holiday
- [ ] DELETE /Holiday/{id}
- [ ] GET /Holiday/{id}

### Hopewiser (1 endpoints)
- [ ] GET /Hopewiser/Get

### ISLOnline (2 endpoints)
- [ ] POST /ISLOnline/CreateLink
- [ ] GET /ISLOnline/Get

### ImpersonationRequest (1 endpoints)
- [ ] POST /ImpersonationRequest

### ImportCSV (4 endpoints)
- [ ] GET /ImportCSV
- [ ] POST /ImportCSV
- [ ] DELETE /ImportCSV/{id}
- [ ] GET /ImportCSV/{id}

### IncomingEvent (5 endpoints)
- [ ] GET /IncomingEvent
- [ ] POST /IncomingEvent
- [ ] POST /IncomingEvent/Process
- [ ] DELETE /IncomingEvent/{id}
- [ ] GET /IncomingEvent/{id}

### IncomingWebhook (5 endpoints)
- [ ] GET /IncomingWebhook
- [ ] POST /IncomingWebhook
- [ ] POST /IncomingWebhook/Process
- [ ] DELETE /IncomingWebhook/{id}
- [ ] GET /IncomingWebhook/{id}

### IncomingWebhookAttempt (1 endpoints)
- [ ] GET /IncomingWebhookAttempt

### IngramMicroDetails (4 endpoints)
- [ ] GET /IngramMicroDetails
- [ ] POST /IngramMicroDetails
- [ ] DELETE /IngramMicroDetails/{id}
- [ ] GET /IngramMicroDetails/{id}

### IngramMicroReseller (2 endpoints)
- [ ] GET /IngramMicroReseller/Get
- [ ] GET /IngramMicroReseller/GetQuote

### IngramMicroResellerDetails (4 endpoints)
- [ ] GET /IngramMicroResellerDetails
- [ ] POST /IngramMicroResellerDetails
- [ ] DELETE /IngramMicroResellerDetails/{id}
- [ ] GET /IngramMicroResellerDetails/{id}

### Instance (3 endpoints)
- [ ] GET /Instance
- [ ] POST /Instance
- [ ] GET /Instance/{id}

### InstanceInfo (1 endpoints)
- [ ] GET /InstanceInfo

### IntegrationConfiguration (3 endpoints)
- [ ] GET /IntegrationConfiguration
- [ ] POST /IntegrationConfiguration
- [ ] GET /IntegrationConfiguration/{id}

### IntegrationData (156 endpoints)
- [ ] POST /IntegrationData/AdjustQty/MicrosoftCSP
- [ ] POST /IntegrationData/AdjustQty/Pax8
- [ ] GET /IntegrationData/BigPanda/GetDeviceList
- [ ] POST /IntegrationData/ClearLicenceKeyCache/MicrosoftCSP
- [ ] POST /IntegrationData/CreateIncident/SplunkOnCall
- [ ] POST /IntegrationData/Export/Lansweeper
- [ ] POST /IntegrationData/FormatJsonArray
- [ ] GET /IntegrationData/Get/AmazonSeller
- [ ] GET /IntegrationData/Get/ArrowSphere
- [ ] GET /IntegrationData/Get/Atera
- [ ] GET /IntegrationData/Get/Automate
- [ ] GET /IntegrationData/Get/Autotask
- [ ] GET /IntegrationData/Get/Auvik
- [ ] GET /IntegrationData/Get/Avalara
- [ ] GET /IntegrationData/Get/AzureAD
- [ ] GET /IntegrationData/Get/AzureAD/Delta
- [ ] GET /IntegrationData/Get/AzureSentinel
- [ ] GET /IntegrationData/Get/Barracuda
- [ ] GET /IntegrationData/Get/BusinessCentral
- [ ] GET /IntegrationData/Get/CloudMarketplace
- [ ] GET /IntegrationData/Get/Confluence
- [ ] GET /IntegrationData/Get/ConnectWise
- [ ] GET /IntegrationData/Get/ConnectwiseControl
- [ ] GET /IntegrationData/Get/ConnectwiseRmm
- [ ] GET /IntegrationData/Get/Datagate
- [ ] GET /IntegrationData/Get/Datto
- [ ] GET /IntegrationData/Get/DattoCommerce
- [ ] GET /IntegrationData/Get/DeletedMail
- [ ] GET /IntegrationData/Get/DevOps
- [ ] GET /IntegrationData/Get/Device42
- [ ] GET /IntegrationData/Get/DickerData
- [ ] GET /IntegrationData/Get/Domotz
- [ ] GET /IntegrationData/Get/DynamicsCRM
- [ ] GET /IntegrationData/Get/Dynatrace
- [ ] GET /IntegrationData/Get/Etilize
- [ ] GET /IntegrationData/Get/ExactOnline
- [ ] GET /IntegrationData/Get/ExchangeCalendars
- [ ] GET /IntegrationData/Get/ExchangeCalendars/EWS
- [ ] GET /IntegrationData/Get/Facebook
- [ ] GET /IntegrationData/Get/Fortnox
- [ ] GET /IntegrationData/Get/Freshdesk
- [ ] GET /IntegrationData/Get/Giacom
- [ ] GET /IntegrationData/Get/GoCardless
- [ ] GET /IntegrationData/Get/GoCardless/Payments
- [ ] GET /IntegrationData/Get/GoToAssist
- [ ] GET /IntegrationData/Get/GoogleBusiness
- [ ] GET /IntegrationData/Get/GoogleCalendars
- [ ] GET /IntegrationData/Get/GoogleWorkplace
- [ ] GET /IntegrationData/Get/HaloLink
- [ ] GET /IntegrationData/Get/HolidayAPI
- [ ] GET /IntegrationData/Get/HubSpot
- [ ] GET /IntegrationData/Get/ITGlue
- [ ] GET /IntegrationData/Get/Icinga
- [ ] GET /IntegrationData/Get/IngramMicro
- [ ] GET /IntegrationData/Get/Intacct
- [ ] GET /IntegrationData/Get/Interact
- [ ] GET /IntegrationData/Get/Intune
- [ ] GET /IntegrationData/Get/Jamf
- [ ] GET /IntegrationData/Get/Jira
- [ ] GET /IntegrationData/Get/JiraServiceManagement
- [ ] GET /IntegrationData/Get/KaseyaVSA
- [ ] GET /IntegrationData/Get/Kashflow
- [ ] GET /IntegrationData/Get/Lansweeper
- [ ] GET /IntegrationData/Get/Liongard
- [ ] GET /IntegrationData/Get/LogMeIn
- [ ] GET /IntegrationData/Get/LogicMonitor
- [ ] GET /IntegrationData/Get/Mail
- [ ] GET /IntegrationData/Get/Mattermost
- [ ] GET /IntegrationData/Get/Meraki
- [ ] GET /IntegrationData/Get/MicrosoftCSP
- [ ] GET /IntegrationData/Get/MicrosoftSkus
- [ ] GET /IntegrationData/Get/Myob
- [ ] GET /IntegrationData/Get/NCentral
- [ ] GET /IntegrationData/Get/NewRelic
- [ ] GET /IntegrationData/Get/NinjaRMM
- [ ] GET /IntegrationData/Get/Okta
- [ ] GET /IntegrationData/Get/PRTG
- [ ] GET /IntegrationData/Get/PagerDuty
- [ ] GET /IntegrationData/Get/Passportal
- [ ] GET /IntegrationData/Get/Pax8
- [ ] GET /IntegrationData/Get/Prometheus
- [ ] GET /IntegrationData/Get/Qualys
- [ ] GET /IntegrationData/Get/QuickBooksOnline
- [ ] GET /IntegrationData/Get/Quoter
- [ ] GET /IntegrationData/Get/Rhipe
- [ ] GET /IntegrationData/Get/SageBusinessCloud
- [ ] GET /IntegrationData/Get/SalesMailbox
- [ ] GET /IntegrationData/Get/SalesMailbox/{id}
- [ ] GET /IntegrationData/Get/Salesforce
- [ ] GET /IntegrationData/Get/ServiceNow
- [ ] GET /IntegrationData/Get/ServiceNowIntegration
- [ ] GET /IntegrationData/Get/Sherweb
- [ ] GET /IntegrationData/Get/Shopify
- [ ] GET /IntegrationData/Get/ShopifyVerify
- [ ] GET /IntegrationData/Get/Slack
- [ ] GET /IntegrationData/Get/SnelStart
- [ ] GET /IntegrationData/Get/SnipeIT
- [ ] GET /IntegrationData/Get/Snow
- [ ] GET /IntegrationData/Get/SolarWindsRMM
- [ ] GET /IntegrationData/Get/Splashtop
- [ ] GET /IntegrationData/Get/SplunkOnCall
- [ ] GET /IntegrationData/Get/StreamOneIon
- [ ] GET /IntegrationData/Get/Stripe
- [ ] GET /IntegrationData/Get/Syncro
- [ ] GET /IntegrationData/Get/Synnex
- [ ] GET /IntegrationData/Get/Tanium
- [ ] GET /IntegrationData/Get/TechData
- [ ] GET /IntegrationData/Get/Twitter
- [ ] GET /IntegrationData/Get/VMWorkspace
- [ ] GET /IntegrationData/Get/WordpressCom
- [ ] GET /IntegrationData/Get/WordpressOrg
- [ ] GET /IntegrationData/Get/Xensam
- [ ] GET /IntegrationData/Get/Xero
- [ ] GET /IntegrationData/Get/Zabbix
- [ ] GET /IntegrationData/Get/intY
- [ ] POST /IntegrationData/Import/BeyondTrust
- [ ] POST /IntegrationData/Import/BusinessCentral
- [ ] POST /IntegrationData/Import/DevOps
- [ ] POST /IntegrationData/Import/ExactOnline
- [ ] POST /IntegrationData/Import/ExchangeCalendars/EWS
- [ ] POST /IntegrationData/Import/Fortnox
- [ ] POST /IntegrationData/Import/IngramMicro/Subscriptions
- [ ] POST /IntegrationData/Import/Intacct
- [ ] POST /IntegrationData/Import/Jira
- [ ] POST /IntegrationData/Import/Kashflow
- [ ] POST /IntegrationData/Import/Myob
- [ ] POST /IntegrationData/Import/QuickBooksOnline
- [ ] POST /IntegrationData/Import/SageBusinessCloud
- [ ] POST /IntegrationData/Import/SnelStart
- [ ] POST /IntegrationData/Import/Xero
- [ ] POST /IntegrationData/Link/DevOps
- [ ] POST /IntegrationData/Link/Jira
- [ ] POST /IntegrationData/MicrosoftTeams/Manifest
- [ ] POST /IntegrationData/Move/Mail
- [ ] POST /IntegrationData/Post/Confluence/create-webhook
- [ ] POST /IntegrationData/Post/GoogleCalendars
- [ ] POST /IntegrationData/Post/Liongard/Customer
- [ ] POST /IntegrationData/Post/Liongard/Metrics
- [ ] POST /IntegrationData/Post/Mattermost/create-webhook
- [ ] POST /IntegrationData/Post/Mattermost/delete-webhook
- [ ] POST /IntegrationData/Post/Mattermost/send-webhook
- [ ] POST /IntegrationData/Post/OpenAi
- [ ] POST /IntegrationData/Post/Stripe/create-payment-intent
- [ ] POST /IntegrationData/Post/Stripe/create-portal-session
- [ ] POST /IntegrationData/Post/Stripe/create-setup-intent
- [ ] POST /IntegrationData/Post/Stripe/create-webhook
- [ ] POST /IntegrationData/Post/Stripe/update-invoice-payment
- [ ] POST /IntegrationData/SAML/IdP/Metadata
- [ ] GET /IntegrationData/SAML/SP/Metadata
- [ ] GET /IntegrationData/Search/DevOps
- [ ] GET /IntegrationData/Search/Jira
- [ ] POST /IntegrationData/Send/Xero
- [ ] POST /IntegrationData/Unlink/DevOps
- [ ] POST /IntegrationData/Unlink/HaloLink
- [ ] POST /IntegrationData/Unlink/Jira
- [ ] GET /IntegrationData/Validate/Jira

### IntegrationDelta (4 endpoints)
- [ ] GET /IntegrationDelta
- [ ] POST /IntegrationDelta
- [ ] DELETE /IntegrationDelta/{id}
- [ ] GET /IntegrationDelta/{id}

### IntegrationError (4 endpoints)
- [ ] GET /IntegrationError
- [ ] POST /IntegrationError
- [ ] DELETE /IntegrationError/{id}
- [ ] GET /IntegrationError/{id}

### IntegrationExport (3 endpoints)
- [ ] GET /IntegrationExport
- [ ] POST /IntegrationExport
- [ ] DELETE /IntegrationExport/{id}

### IntegrationFieldData (4 endpoints)
- [ ] GET /IntegrationFieldData
- [ ] POST /IntegrationFieldData
- [ ] DELETE /IntegrationFieldData/{id}
- [ ] GET /IntegrationFieldData/{id}

### IntegrationFieldMapping (1 endpoints)
- [ ] GET /IntegrationFieldMapping

### IntegrationLookUp (2 endpoints)
- [ ] GET /IntegrationLookUp
- [ ] POST /IntegrationLookUp

### IntegrationRequest (4 endpoints)
- [ ] GET /IntegrationRequest
- [ ] POST /IntegrationRequest
- [ ] DELETE /IntegrationRequest/{id}
- [ ] GET /IntegrationRequest/{id}

### IntegrationRunbookVariableGroup (2 endpoints)
- [ ] GET /IntegrationRunbookVariableGroup
- [ ] GET /IntegrationRunbookVariableGroup/{id}

### IntegrationSiteMapping (1 endpoints)
- [ ] GET /IntegrationSiteMapping

### IntegratorLog (1 endpoints)
- [ ] GET /IntegratorLog

### IntegratorSchedule (1 endpoints)
- [ ] GET /IntegratorSchedule

### IntegratorTrace (2 endpoints)
- [ ] GET /IntegratorTrace
- [ ] GET /IntegratorTrace/{id}

### Invoice (9 endpoints) ⭐ CORE
- [ ] GET /Invoice
- [ ] POST /Invoice
- [ ] POST /Invoice/PDF/{id}
- [ ] POST /Invoice/View
- [ ] GET /Invoice/lines
- [ ] POST /Invoice/updatelines
- [ ] DELETE /Invoice/{id}
- [ ] GET /Invoice/{id}
- [ ] POST /Invoice/{id}/void

### InvoiceChange (2 endpoints)
- [ ] GET /InvoiceChange
- [ ] POST /InvoiceChange

### InvoiceDetailProRata (1 endpoints)
- [ ] GET /InvoiceDetailProRata

### InvoicePayment (4 endpoints)
- [ ] GET /InvoicePayment
- [ ] POST /InvoicePayment
- [ ] DELETE /InvoicePayment/{id}
- [ ] GET /InvoicePayment/{id}

### Item (5 endpoints) ⭐ CORE
- [ ] GET /Item
- [ ] POST /Item
- [ ] POST /Item/NewAccountsId
- [ ] DELETE /Item/{id}
- [ ] GET /Item/{id}

### ItemAccountsLink (5 endpoints)
- [ ] GET /ItemAccountsLink
- [ ] POST /ItemAccountsLink
- [ ] POST /ItemAccountsLink/Migrate
- [ ] DELETE /ItemAccountsLink/{id}
- [ ] GET /ItemAccountsLink/{id}

### ItemGroup (4 endpoints)
- [ ] GET /ItemGroup
- [ ] POST /ItemGroup
- [ ] DELETE /ItemGroup/{id}
- [ ] GET /ItemGroup/{id}

### ItemStock (4 endpoints)
- [ ] GET /ItemStock
- [ ] POST /ItemStock
- [ ] DELETE /ItemStock/{id}
- [ ] GET /ItemStock/{id}

### ItemStockHistory (2 endpoints)
- [ ] GET /ItemStockHistory
- [ ] GET /ItemStockHistory/{id}

### JamfDetails (4 endpoints)
- [ ] GET /JamfDetails
- [ ] POST /JamfDetails
- [ ] DELETE /JamfDetails/{id}
- [ ] GET /JamfDetails/{id}

### JiraDetails (4 endpoints)
- [ ] GET /JiraDetails
- [ ] POST /JiraDetails
- [ ] DELETE /JiraDetails/{id}
- [ ] GET /JiraDetails/{id}

### Journey (4 endpoints)
- [ ] GET /Journey
- [ ] POST /Journey
- [ ] DELETE /Journey/{id}
- [ ] GET /Journey/{id}

### KBArticle (5 endpoints) ⭐ CORE
- [ ] GET /KBArticle
- [ ] POST /KBArticle
- [ ] POST /KBArticle/vote
- [ ] DELETE /KBArticle/{id}
- [ ] GET /KBArticle/{id}

### KBArticleAnon (2 endpoints)
- [ ] GET /KBArticleAnon
- [ ] GET /KBArticleAnon/{slug}

### Kandji (1 endpoints)
- [ ] GET /Kandji/Get

### KandjiDetails (4 endpoints)
- [ ] GET /KandjiDetails
- [ ] POST /KandjiDetails
- [ ] DELETE /KandjiDetails/{id}
- [ ] GET /KandjiDetails/{id}

### KaseyaVSAX (3 endpoints)
- [ ] POST /KaseyaVSAX/CreateWebhook/{detailsId}
- [ ] DELETE /KaseyaVSAX/DeleteWebhook/{detailsId}
- [ ] GET /KaseyaVSAX/Get

### KaseyaVSAXDetails (4 endpoints)
- [ ] GET /KaseyaVSAXDetails
- [ ] POST /KaseyaVSAXDetails
- [ ] DELETE /KaseyaVSAXDetails/{id}
- [ ] GET /KaseyaVSAXDetails/{id}

### KashflowDetails (4 endpoints)
- [ ] GET /KashflowDetails
- [ ] POST /KashflowDetails
- [ ] DELETE /KashflowDetails/{id}
- [ ] GET /KashflowDetails/{id}

### KeyVault (4 endpoints)
- [ ] GET /KeyVault
- [ ] POST /KeyVault
- [ ] DELETE /KeyVault/{id}
- [ ] GET /KeyVault/{id}

### LDAPConnection (4 endpoints)
- [ ] GET /LDAPConnection
- [ ] POST /LDAPConnection
- [ ] DELETE /LDAPConnection/{id}
- [ ] GET /LDAPConnection/{id}

### Languages (4 endpoints)
- [ ] GET /Languages
- [ ] POST /Languages
- [ ] DELETE /Languages/{id}
- [ ] GET /Languages/{id}

### LapSafe (3 endpoints)
- [ ] GET /LapSafe/Cancel
- [ ] GET /LapSafe/Complete
- [ ] GET /LapSafe/Get

### LicenceChange (1 endpoints)
- [ ] GET /LicenceChange

### LicenseInfo (3 endpoints)
- [ ] GET /LicenseInfo
- [ ] POST /LicenseInfo
- [ ] GET /LicenseInfo/password

### LoginToken (1 endpoints)
- [ ] POST /LoginToken

### Lookup (5 endpoints)
- [ ] GET /Lookup
- [ ] POST /Lookup
- [ ] POST /Lookup/ClearCache
- [ ] DELETE /Lookup/{id}
- [ ] GET /Lookup/{id}

### MO (6 endpoints)
- [ ] GET /MO
- [ ] POST /MO
- [ ] GET /MO/b
- [ ] GET /MO/r
- [ ] DELETE /MO/{id}
- [ ] GET /MO/{id}

### MYOBdetails (4 endpoints)
- [ ] GET /MYOBdetails
- [ ] POST /MYOBdetails
- [ ] DELETE /MYOBdetails/{id}
- [ ] GET /MYOBdetails/{id}

### Mail (6 endpoints)
- [ ] POST /Mail/Azure
- [ ] POST /Mail/Integrator/Azure
- [ ] POST /Mail/Integrator/Google
- [ ] POST /Mail/Integrator/IMAP
- [ ] POST /Mail/Integrator/Pop3
- [ ] POST /Mail/ProcessMail

### MailCampaign (4 endpoints)
- [ ] GET /MailCampaign
- [ ] POST /MailCampaign
- [ ] DELETE /MailCampaign/{id}
- [ ] GET /MailCampaign/{id}

### MailCampaignEmail (4 endpoints)
- [ ] GET /MailCampaignEmail
- [ ] POST /MailCampaignEmail
- [ ] DELETE /MailCampaignEmail/{id}
- [ ] GET /MailCampaignEmail/{id}

### MailCampaignLog (2 endpoints)
- [ ] GET /MailCampaignLog
- [ ] GET /MailCampaignLog/{id}

### Mailbox (5 endpoints)
- [ ] GET /Mailbox
- [ ] POST /Mailbox
- [ ] DELETE /Mailbox/{id}
- [ ] GET /Mailbox/{id}
- [ ] GET /Mailbox/{id}/OutlookContacts

### MailboxCredential (4 endpoints)
- [ ] GET /MailboxCredential
- [ ] POST /MailboxCredential
- [ ] DELETE /MailboxCredential/{id}
- [ ] GET /MailboxCredential/{id}

### Mailchimp (1 endpoints)
- [ ] GET /Mailchimp/Get

### ManageEngine (1 endpoints)
- [ ] GET /ManageEngine/Get

### ManageEngineDetails (4 endpoints)
- [ ] GET /ManageEngineDetails
- [ ] POST /ManageEngineDetails
- [ ] DELETE /ManageEngineDetails/{id}
- [ ] GET /ManageEngineDetails/{id}

### MarketingUnsubscribe (4 endpoints)
- [ ] GET /MarketingUnsubscribe
- [ ] POST /MarketingUnsubscribe
- [ ] DELETE /MarketingUnsubscribe/{id}
- [ ] GET /MarketingUnsubscribe/{id}

### MattermostChannelDetails (1 endpoints)
- [ ] GET /MattermostChannelDetails

### MattermostDetails (4 endpoints)
- [ ] GET /MattermostDetails
- [ ] POST /MattermostDetails
- [ ] DELETE /MattermostDetails/{id}
- [ ] GET /MattermostDetails/{id}

### MeterReading (3 endpoints)
- [ ] GET /MeterReading
- [ ] POST /MeterReading
- [ ] GET /MeterReading/{id}

### MicrosoftSubscriptionMapping (4 endpoints)
- [ ] GET /MicrosoftSubscriptionMapping
- [ ] POST /MicrosoftSubscriptionMapping
- [ ] DELETE /MicrosoftSubscriptionMapping/{id}
- [ ] GET /MicrosoftSubscriptionMapping/{id}

### MicrosoftTeams (1 endpoints)
- [ ] GET /MicrosoftTeams/Get

### MicrosoftTeamsMapping (4 endpoints)
- [ ] GET /MicrosoftTeamsMapping
- [ ] POST /MicrosoftTeamsMapping
- [ ] DELETE /MicrosoftTeamsMapping/{id}
- [ ] GET /MicrosoftTeamsMapping/{id}

### NCentralDetails (4 endpoints)
- [ ] GET /NCentralDetails
- [ ] POST /NCentralDetails
- [ ] DELETE /NCentralDetails/{id}
- [ ] GET /NCentralDetails/{id}

### Nhserverconfig (4 endpoints)
- [ ] GET /Nhserverconfig
- [ ] POST /Nhserverconfig
- [ ] DELETE /Nhserverconfig/{id}
- [ ] GET /Nhserverconfig/{id}

### Notification (4 endpoints)
- [ ] GET /Notification
- [ ] POST /Notification
- [ ] DELETE /Notification/{id}
- [ ] GET /Notification/{id}

### NotificationLog (1 endpoints)
- [ ] GET /NotificationLog

### NotificationMessage (4 endpoints)
- [ ] GET /NotificationMessage
- [ ] POST /NotificationMessage
- [ ] DELETE /NotificationMessage/{id}
- [ ] GET /NotificationMessage/{id}

### Notifications (5 endpoints)
- [ ] GET /Notifications
- [ ] POST /Notifications
- [ ] POST /Notifications/process
- [ ] DELETE /Notifications/{id}
- [ ] GET /Notifications/{id}

### ObjectMappingProfile (1 endpoints)
- [ ] GET /ObjectMappingProfile

### OnlineStatus (2 endpoints)
- [ ] GET /OnlineStatus
- [ ] POST /OnlineStatus

### Opportunities (5 endpoints) ⭐ CORE
- [ ] GET /Opportunities
- [ ] POST /Opportunities
- [ ] POST /Opportunities/View
- [ ] DELETE /Opportunities/{id}
- [ ] GET /Opportunities/{id}

### OrderLine (1 endpoints)
- [ ] GET /OrderLine

### Organisation (4 endpoints)
- [ ] GET /Organisation
- [ ] POST /Organisation
- [ ] DELETE /Organisation/{id}
- [ ] GET /Organisation/{id}

### Outcome (4 endpoints)
- [ ] GET /Outcome
- [ ] POST /Outcome
- [ ] DELETE /Outcome/{id}
- [ ] GET /Outcome/{id}

### Outgoing (4 endpoints)
- [ ] GET /Outgoing
- [ ] POST /Outgoing
- [ ] DELETE /Outgoing/{id}
- [ ] GET /Outgoing/{id}

### OutgoingAttempt (2 endpoints)
- [ ] GET /OutgoingAttempt
- [ ] GET /OutgoingAttempt/{id}

### Outgoingemail (3 endpoints)
- [ ] GET /Outgoingemail
- [ ] POST /Outgoingemail
- [ ] DELETE /Outgoingemail/{id}

### PRTGDetails (4 endpoints)
- [ ] GET /PRTGDetails
- [ ] POST /PRTGDetails
- [ ] DELETE /PRTGDetails/{id}
- [ ] GET /PRTGDetails/{id}

### PasswordField (3 endpoints)
- [ ] GET /PasswordField
- [ ] POST /PasswordField
- [ ] GET /PasswordField/{id}

### Pax8Details (4 endpoints)
- [ ] GET /Pax8Details
- [ ] POST /Pax8Details
- [ ] DELETE /Pax8Details/{id}
- [ ] GET /Pax8Details/{id}

### PdfTemplate (4 endpoints)
- [ ] GET /PdfTemplate
- [ ] POST /PdfTemplate
- [ ] DELETE /PdfTemplate/{id}
- [ ] GET /PdfTemplate/{id}

### PdfTemplateRepository (2 endpoints)
- [ ] GET /PdfTemplateRepository
- [ ] GET /PdfTemplateRepository/{id}

### PopupNote (2 endpoints)
- [ ] GET /PopupNote
- [ ] POST /PopupNote/read

### PowerShellScript (4 endpoints)
- [ ] GET /PowerShellScript
- [ ] POST /PowerShellScript
- [ ] DELETE /PowerShellScript/{id}
- [ ] GET /PowerShellScript/{id}

### PowerShellScriptCriteria (4 endpoints)
- [ ] GET /PowerShellScriptCriteria
- [ ] POST /PowerShellScriptCriteria
- [ ] DELETE /PowerShellScriptCriteria/{id}
- [ ] GET /PowerShellScriptCriteria/{id}

### PowerShellScriptProcessing (4 endpoints)
- [ ] GET /PowerShellScriptProcessing
- [ ] POST /PowerShellScriptProcessing
- [ ] DELETE /PowerShellScriptProcessing/{id}
- [ ] GET /PowerShellScriptProcessing/{id}

### Priority (4 endpoints) ⭐ CORE
- [ ] GET /Priority
- [ ] POST /Priority
- [ ] DELETE /Priority/{id}
- [ ] GET /Priority/{id}

### Product (4 endpoints)
- [ ] GET /Product
- [ ] POST /Product
- [ ] DELETE /Product/{id}
- [ ] GET /Product/{id}

### ProductBranch (1 endpoints)
- [ ] GET /ProductBranch

### ProductComponent (4 endpoints)
- [ ] GET /ProductComponent
- [ ] POST /ProductComponent
- [ ] DELETE /ProductComponent/{id}
- [ ] GET /ProductComponent/{id}

### ProjectSetupLines (1 endpoints)
- [ ] POST /ProjectSetupLines

### Projects (5 endpoints) ⭐ CORE
- [ ] GET /Projects
- [ ] POST /Projects
- [ ] POST /Projects/View
- [ ] DELETE /Projects/{id}
- [ ] GET /Projects/{id}

### PublishProfiles (4 endpoints)
- [ ] GET /PublishProfiles
- [ ] POST /PublishProfiles
- [ ] DELETE /PublishProfiles/{id}
- [ ] GET /PublishProfiles/{id}

### PurchaseOrder (6 endpoints)
- [ ] GET /PurchaseOrder
- [ ] POST /PurchaseOrder
- [ ] POST /PurchaseOrder/View
- [ ] POST /PurchaseOrder/confirmreceipt
- [ ] DELETE /PurchaseOrder/{id}
- [ ] GET /PurchaseOrder/{id}

### Qualification (4 endpoints)
- [ ] GET /Qualification
- [ ] POST /Qualification
- [ ] DELETE /Qualification/{id}
- [ ] GET /Qualification/{id}

### QuickBooksDetails (4 endpoints)
- [ ] GET /QuickBooksDetails
- [ ] POST /QuickBooksDetails
- [ ] DELETE /QuickBooksDetails/{id}
- [ ] GET /QuickBooksDetails/{id}

### Quotation (7 endpoints) ⭐ CORE
- [ ] GET /Quotation
- [ ] POST /Quotation
- [ ] POST /Quotation/Approval
- [ ] POST /Quotation/Lines
- [ ] POST /Quotation/View
- [ ] DELETE /Quotation/{id}
- [ ] GET /Quotation/{id}

### Raynet (1 endpoints)
- [ ] GET /Raynet/Get

### RaynetDetails (4 endpoints)
- [ ] GET /RaynetDetails
- [ ] POST /RaynetDetails
- [ ] DELETE /RaynetDetails/{id}
- [ ] GET /RaynetDetails/{id}

### RecurringInvoice (7 endpoints)
- [ ] GET /RecurringInvoice
- [ ] POST /RecurringInvoice
- [ ] POST /RecurringInvoice/Lines
- [ ] POST /RecurringInvoice/process
- [ ] POST /RecurringInvoice/updatelines
- [ ] DELETE /RecurringInvoice/{id}
- [ ] GET /RecurringInvoice/{id}

### RecurringItem (1 endpoints)
- [ ] GET /RecurringItem

### Release (4 endpoints) ⭐ CORE
- [ ] GET /Release
- [ ] POST /Release
- [ ] DELETE /Release/{id}
- [ ] GET /Release/{id}

### ReleaseNoteGroup (4 endpoints)
- [ ] GET /ReleaseNoteGroup
- [ ] POST /ReleaseNoteGroup
- [ ] DELETE /ReleaseNoteGroup/{id}
- [ ] GET /ReleaseNoteGroup/{id}

### ReleasePipeline (4 endpoints)
- [ ] GET /ReleasePipeline
- [ ] POST /ReleasePipeline
- [ ] DELETE /ReleasePipeline/{id}
- [ ] GET /ReleasePipeline/{id}

### ReleaseType (4 endpoints)
- [ ] GET /ReleaseType
- [ ] POST /ReleaseType
- [ ] DELETE /ReleaseType/{id}
- [ ] GET /ReleaseType/{id}

### RemoteSession (4 endpoints)
- [ ] GET /RemoteSession
- [ ] POST /RemoteSession
- [ ] DELETE /RemoteSession/{id}
- [ ] GET /RemoteSession/{id}

### RemoteSessionTeams (1 endpoints)
- [ ] GET /RemoteSessionTeams

### Report (7 endpoints) ⭐ CORE
- [ ] GET /Report
- [ ] POST /Report
- [ ] POST /Report/Bookmark
- [ ] POST /Report/createpdf
- [ ] POST /Report/print
- [ ] DELETE /Report/{id}
- [ ] GET /Report/{id}

### ReportData (1 endpoints)
- [ ] GET /ReportData/{publishedid}

### ReportRepository (3 endpoints)
- [ ] GET /ReportRepository
- [ ] GET /ReportRepository/ReportCategories
- [ ] GET /ReportRepository/{id}

### ResourceType (2 endpoints)
- [ ] GET /ResourceType
- [ ] GET /ResourceType/{id}

### Roadmap (1 endpoints)
- [ ] GET /Roadmap

### Roles (4 endpoints)
- [ ] GET /Roles
- [ ] POST /Roles
- [ ] DELETE /Roles/{id}
- [ ] GET /Roles/{id}

### SLA (4 endpoints) ⭐ CORE
- [ ] GET /SLA
- [ ] POST /SLA
- [ ] DELETE /SLA/{id}
- [ ] GET /SLA/{id}

### SQLImport (4 endpoints)
- [ ] GET /SQLImport
- [ ] POST /SQLImport
- [ ] DELETE /SQLImport/{id}
- [ ] GET /SQLImport/{id}

### SageBusinessCloudDetails (4 endpoints)
- [ ] GET /SageBusinessCloudDetails
- [ ] POST /SageBusinessCloudDetails
- [ ] DELETE /SageBusinessCloudDetails/{id}
- [ ] GET /SageBusinessCloudDetails/{id}

### SailPointDetails (4 endpoints)
- [ ] GET /SailPointDetails
- [ ] POST /SailPointDetails
- [ ] DELETE /SailPointDetails/{id}
- [ ] GET /SailPointDetails/{id}

### SailPointRoleMapping (1 endpoints)
- [ ] GET /SailPointRoleMapping

### SailPointUserMapping (1 endpoints)
- [ ] GET /SailPointUserMapping

### SalesMailbox (4 endpoints)
- [ ] GET /SalesMailbox
- [ ] POST /SalesMailbox
- [ ] DELETE /SalesMailbox/{id}
- [ ] GET /SalesMailbox/{id}

### SalesMailboxDetail (2 endpoints)
- [ ] GET /SalesMailboxDetail
- [ ] POST /SalesMailboxDetail

### SalesOrder (5 endpoints)
- [ ] GET /SalesOrder
- [ ] POST /SalesOrder
- [ ] POST /SalesOrder/View
- [ ] DELETE /SalesOrder/{id}
- [ ] GET /SalesOrder/{id}

### SavedForecast (4 endpoints)
- [ ] GET /SavedForecast
- [ ] POST /SavedForecast
- [ ] DELETE /SavedForecast/{id}
- [ ] GET /SavedForecast/{id}

### Schedule (3 endpoints)
- [ ] GET /Schedule
- [ ] POST /Schedule
- [ ] GET /Schedule/{id}

### ScheduleOccurrence (3 endpoints)
- [ ] GET /ScheduleOccurrence
- [ ] POST /ScheduleOccurrence
- [ ] GET /ScheduleOccurrence/{id}

### ScreenLayout (4 endpoints)
- [ ] GET /ScreenLayout
- [ ] POST /ScreenLayout
- [ ] DELETE /ScreenLayout/{id}
- [ ] GET /ScreenLayout/{id}

### Search (1 endpoints)
- [ ] GET /Search

### SecureSecretLink (5 endpoints)
- [ ] GET /SecureSecretLink
- [ ] POST /SecureSecretLink
- [ ] GET /SecureSecretLink/validate
- [ ] DELETE /SecureSecretLink/{id}
- [ ] GET /SecureSecretLink/{id}

### SecurityCheck (2 endpoints)
- [ ] GET /SecurityCheck
- [ ] GET /SecurityCheck/oldencryption

### SecurityQuestion (4 endpoints)
- [ ] GET /SecurityQuestion
- [ ] POST /SecurityQuestion
- [ ] DELETE /SecurityQuestion/{id}
- [ ] GET /SecurityQuestion/{id}

### SecurityQuestionValidate (2 endpoints)
- [ ] GET /SecurityQuestionValidate
- [ ] POST /SecurityQuestionValidate

### SentinelOne (1 endpoints)
- [ ] GET /SentinelOne/Get

### SentinelOneDetails (4 endpoints)
- [ ] GET /SentinelOneDetails
- [ ] POST /SentinelOneDetails
- [ ] DELETE /SentinelOneDetails/{id}
- [ ] GET /SentinelOneDetails/{id}

### Service (5 endpoints)
- [ ] GET /Service
- [ ] POST /Service
- [ ] POST /Service/unsubscribe
- [ ] DELETE /Service/{id}
- [ ] GET /Service/{id}

### ServiceAvailability (4 endpoints)
- [ ] GET /ServiceAvailability
- [ ] POST /ServiceAvailability
- [ ] DELETE /ServiceAvailability/{id}
- [ ] GET /ServiceAvailability/{id}

### ServiceCategory (4 endpoints)
- [ ] GET /ServiceCategory
- [ ] POST /ServiceCategory
- [ ] DELETE /ServiceCategory/{id}
- [ ] GET /ServiceCategory/{id}

### ServiceRequestDetails (2 endpoints)
- [ ] GET /ServiceRequestDetails
- [ ] GET /ServiceRequestDetails/{id}

### ServiceRestriction (1 endpoints)
- [ ] GET /ServiceRestriction

### ServiceStatus (6 endpoints)
- [ ] GET /ServiceStatus
- [ ] POST /ServiceStatus
- [ ] POST /ServiceStatus/Subscribe
- [ ] GET /ServiceStatus/Subscribe/{id}
- [ ] DELETE /ServiceStatus/{id}
- [ ] GET /ServiceStatus/{id}

### SetupTab (3 endpoints)
- [ ] GET /SetupTab
- [ ] POST /SetupTab
- [ ] GET /SetupTab/{id}

### SetupTabGroup (2 endpoints)
- [ ] GET /SetupTabGroup
- [ ] GET /SetupTabGroup/{id}

### SharePoint (1 endpoints)
- [ ] GET /SharePoint/Get

### ShopifyDetails (4 endpoints)
- [ ] GET /ShopifyDetails
- [ ] POST /ShopifyDetails
- [ ] DELETE /ShopifyDetails/{id}
- [ ] GET /ShopifyDetails/{id}

### SingleSignOnApplication (4 endpoints)
- [ ] GET /SingleSignOnApplication
- [ ] POST /SingleSignOnApplication
- [ ] DELETE /SingleSignOnApplication/{id}
- [ ] GET /SingleSignOnApplication/{id}

### SingleSignOnAttempt (3 endpoints)
- [ ] GET /SingleSignOnAttempt
- [ ] DELETE /SingleSignOnAttempt/{id}
- [ ] GET /SingleSignOnAttempt/{id}

### Site (5 endpoints) ⭐ CORE
- [ ] GET /Site
- [ ] POST /Site
- [ ] GET /Site/StockBins
- [ ] DELETE /Site/{id}
- [ ] GET /Site/{id}

### Slack (4 endpoints)
- [ ] POST /Slack/Command
- [ ] POST /Slack/Event
- [ ] POST /Slack/Interactivity
- [ ] POST /Slack/Manifest

### SlackChatApp (4 endpoints)
- [ ] GET /SlackChatApp
- [ ] POST /SlackChatApp
- [ ] DELETE /SlackChatApp/{id}
- [ ] GET /SlackChatApp/{id}

### SlackDetails (5 endpoints)
- [ ] GET /SlackDetails
- [ ] POST /SlackDetails
- [ ] POST /SlackDetails/Uninstall
- [ ] DELETE /SlackDetails/{id}
- [ ] GET /SlackDetails/{id}

### SnipeITDetails (4 endpoints)
- [ ] GET /SnipeITDetails
- [ ] POST /SnipeITDetails
- [ ] DELETE /SnipeITDetails/{id}
- [ ] GET /SnipeITDetails/{id}

### SnowDetails (4 endpoints)
- [ ] GET /SnowDetails
- [ ] POST /SnowDetails
- [ ] DELETE /SnowDetails/{id}
- [ ] GET /SnowDetails/{id}

### SoftwareLicence (4 endpoints) ⭐ CORE
- [ ] GET /SoftwareLicence
- [ ] POST /SoftwareLicence
- [ ] DELETE /SoftwareLicence/{id}
- [ ] GET /SoftwareLicence/{id}

### SoftwareLicenceRole (1 endpoints)
- [ ] GET /SoftwareLicenceRole

### Sophos (1 endpoints)
- [ ] GET /Sophos/Get

### SophosDetails (4 endpoints)
- [ ] GET /SophosDetails
- [ ] POST /SophosDetails
- [ ] DELETE /SophosDetails/{id}
- [ ] GET /SophosDetails/{id}

### Status (4 endpoints) ⭐ CORE
- [ ] GET /Status
- [ ] POST /Status
- [ ] DELETE /Status/{id}
- [ ] GET /Status/{id}

### StockBin (4 endpoints)
- [ ] GET /StockBin
- [ ] POST /StockBin
- [ ] DELETE /StockBin/{id}
- [ ] GET /StockBin/{id}

### StockTrace (2 endpoints)
- [ ] GET /StockTrace
- [ ] GET /StockTrace/{id}

### StreamOneIonDetails (4 endpoints)
- [ ] GET /StreamOneIonDetails
- [ ] POST /StreamOneIonDetails
- [ ] DELETE /StreamOneIonDetails/{id}
- [ ] GET /StreamOneIonDetails/{id}

### StyleProfile (4 endpoints)
- [ ] GET /StyleProfile
- [ ] POST /StyleProfile
- [ ] DELETE /StyleProfile/{id}
- [ ] GET /StyleProfile/{id}

### Supplier (4 endpoints) ⭐ CORE
- [ ] GET /Supplier
- [ ] POST /Supplier
- [ ] DELETE /Supplier/{id}
- [ ] GET /Supplier/{id}

### SupplierContract (5 endpoints)
- [ ] GET /SupplierContract
- [ ] POST /SupplierContract
- [ ] POST /SupplierContract/NextRef
- [ ] DELETE /SupplierContract/{id}
- [ ] GET /SupplierContract/{id}

### SynnexDetails (4 endpoints)
- [ ] GET /SynnexDetails
- [ ] POST /SynnexDetails
- [ ] DELETE /SynnexDetails/{id}
- [ ] GET /SynnexDetails/{id}

### Tabs (4 endpoints)
- [ ] GET /Tabs
- [ ] POST /Tabs
- [ ] DELETE /Tabs/{id}
- [ ] GET /Tabs/{id}

### Tags (4 endpoints)
- [ ] GET /Tags
- [ ] POST /Tags
- [ ] DELETE /Tags/{id}
- [ ] GET /Tags/{id}

### TaniumDetails (4 endpoints)
- [ ] GET /TaniumDetails
- [ ] POST /TaniumDetails
- [ ] DELETE /TaniumDetails/{id}
- [ ] GET /TaniumDetails/{id}

### TaskMonitorEvent (1 endpoints)
- [ ] GET /TaskMonitorEvent

### TaskSchedule (2 endpoints)
- [ ] GET /TaskSchedule
- [ ] POST /TaskSchedule

### TaskTrace (2 endpoints)
- [ ] GET /TaskTrace
- [ ] GET /TaskTrace/{id}

### Tax (4 endpoints)
- [ ] GET /Tax
- [ ] POST /Tax
- [ ] DELETE /Tax/{id}
- [ ] GET /Tax/{id}

### TaxRule (4 endpoints)
- [ ] GET /TaxRule
- [ ] POST /TaxRule
- [ ] DELETE /TaxRule/{id}
- [ ] GET /TaxRule/{id}

### Team (5 endpoints) ⭐ CORE
- [ ] GET /Team
- [ ] POST /Team
- [ ] GET /Team/Tree
- [ ] DELETE /Team/{id}
- [ ] GET /Team/{id}

### TeamImage (1 endpoints)
- [ ] GET /TeamImage/{id}

### TechDataResellerDetails (4 endpoints)
- [ ] GET /TechDataResellerDetails
- [ ] POST /TechDataResellerDetails
- [ ] DELETE /TechDataResellerDetails/{id}
- [ ] GET /TechDataResellerDetails/{id}

### Template (4 endpoints)
- [ ] GET /Template
- [ ] POST /Template
- [ ] DELETE /Template/{id}
- [ ] GET /Template/{id}

### Tenable (4 endpoints)
- [ ] POST /Tenable/Cancel
- [ ] POST /Tenable/Export
- [ ] GET /Tenable/Get
- [ ] GET /Tenable/Status

### TenableDetails (4 endpoints)
- [ ] GET /TenableDetails
- [ ] POST /TenableDetails
- [ ] DELETE /TenableDetails/{id}
- [ ] GET /TenableDetails/{id}

### Tenant (2 endpoints)
- [ ] GET /Tenant
- [ ] POST /Tenant

### Test1 (1 endpoints)
- [ ] GET /Test1

### Test3 (1 endpoints)
- [ ] GET /Test3

### Test4 (1 endpoints)
- [ ] GET /Test4

### TestError (1 endpoints)
- [ ] GET /TestError

### TicketApproval (4 endpoints)
- [ ] GET /TicketApproval
- [ ] POST /TicketApproval
- [ ] GET /TicketApproval/{id}
- [ ] DELETE /TicketApproval/{id}&{seq}

### TicketArea (4 endpoints)
- [ ] GET /TicketArea
- [ ] POST /TicketArea
- [ ] DELETE /TicketArea/{id}
- [ ] GET /TicketArea/{id}

### TicketRules (4 endpoints)
- [ ] GET /TicketRules
- [ ] POST /TicketRules
- [ ] DELETE /TicketRules/{id}
- [ ] GET /TicketRules/{id}

### TicketType (4 endpoints) ⭐ CORE
- [ ] GET /TicketType
- [ ] POST /TicketType
- [ ] DELETE /TicketType/{id}
- [ ] GET /TicketType/{id}

### TicketTypeField (1 endpoints)
- [ ] GET /TicketTypeField

### TicketTypeGroup (4 endpoints)
- [ ] GET /TicketTypeGroup
- [ ] POST /TicketTypeGroup
- [ ] DELETE /TicketTypeGroup/{id}
- [ ] GET /TicketTypeGroup/{id}

### Tickets (11 endpoints) ⭐ CORE
- [ ] GET /Tickets
- [ ] POST /Tickets
- [ ] POST /Tickets/Object
- [ ] POST /Tickets/SetBillableProject
- [ ] POST /Tickets/View
- [ ] POST /Tickets/processchildren
- [ ] GET /Tickets/salesmailbox
- [ ] POST /Tickets/vote
- [ ] GET /Tickets/zapier
- [ ] DELETE /Tickets/{id}
- [ ] GET /Tickets/{id}

### Timesheet (5 endpoints) ⭐ CORE
- [ ] GET /Timesheet
- [ ] POST /Timesheet
- [ ] GET /Timesheet/forecasting
- [ ] GET /Timesheet/mine
- [ ] GET /Timesheet/{id}

### TimesheetEvent (5 endpoints)
- [ ] GET /TimesheetEvent
- [ ] POST /TimesheetEvent
- [ ] GET /TimesheetEvent/mine
- [ ] DELETE /TimesheetEvent/{id}
- [ ] GET /TimesheetEvent/{id}

### Timeslot (1 endpoints)
- [ ] GET /Timeslot

### ToDo (2 endpoints)
- [ ] GET /ToDo
- [ ] POST /ToDo

### ToDoGroup (4 endpoints)
- [ ] GET /ToDoGroup
- [ ] POST /ToDoGroup
- [ ] DELETE /ToDoGroup/{id}
- [ ] GET /ToDoGroup/{id}

### TopLevel (4 endpoints) ⭐ CORE
- [ ] GET /TopLevel
- [ ] POST /TopLevel
- [ ] DELETE /TopLevel/{id}
- [ ] GET /TopLevel/{id}

### TranscriptionStore (4 endpoints)
- [ ] GET /TranscriptionStore
- [ ] POST /TranscriptionStore
- [ ] DELETE /TranscriptionStore/{id}
- [ ] GET /TranscriptionStore/{id}

### Translation (2 endpoints)
- [ ] GET /Translation
- [ ] POST /Translation

### Twilio (2 endpoints)
- [ ] POST /Twilio/callback
- [ ] POST /Twilio/twiml

### TwilioDetails (1 endpoints)
- [ ] GET /TwilioDetails

### TwilioWhatsAppDetails (4 endpoints)
- [ ] GET /TwilioWhatsAppDetails
- [ ] POST /TwilioWhatsAppDetails
- [ ] DELETE /TwilioWhatsAppDetails/{id}
- [ ] GET /TwilioWhatsAppDetails/{id}

### TwitterDetails (4 endpoints)
- [ ] GET /TwitterDetails
- [ ] POST /TwitterDetails
- [ ] DELETE /TwitterDetails/{id}
- [ ] GET /TwitterDetails/{id}

### UnsubServiceEmails (4 endpoints)
- [ ] GET /UnsubServiceEmails
- [ ] POST /UnsubServiceEmails
- [ ] DELETE /UnsubServiceEmails/{id}
- [ ] GET /UnsubServiceEmails/{id}

### UserChange (1 endpoints)
- [ ] GET /UserChange

### UserRoles (4 endpoints)
- [ ] GET /UserRoles
- [ ] POST /UserRoles
- [ ] DELETE /UserRoles/{id}
- [ ] GET /UserRoles/{id}

### Users (6 endpoints) ⭐ CORE
- [ ] GET /Users
- [ ] POST /Users
- [ ] GET /Users/me
- [ ] POST /Users/prefs
- [ ] DELETE /Users/{id}
- [ ] GET /Users/{id}

### VMWorkspaceDetails (4 endpoints)
- [ ] GET /VMWorkspaceDetails
- [ ] POST /VMWorkspaceDetails
- [ ] DELETE /VMWorkspaceDetails/{id}
- [ ] GET /VMWorkspaceDetails/{id}

### VersionInfo (6 endpoints)
- [ ] GET /VersionInfo
- [ ] GET /VersionInfo/GetOneSpotlight/{id}
- [ ] GET /VersionInfo/IntegratorHash
- [ ] GET /VersionInfo/SearchVersionInfo
- [ ] GET /VersionInfo/Spotlight
- [ ] GET /VersionInfo/{id}

### ViewColumns (4 endpoints)
- [ ] GET /ViewColumns
- [ ] POST /ViewColumns
- [ ] DELETE /ViewColumns/{id}
- [ ] GET /ViewColumns/{id}

### ViewFilter (4 endpoints)
- [ ] GET /ViewFilter
- [ ] POST /ViewFilter
- [ ] DELETE /ViewFilter/{id}
- [ ] GET /ViewFilter/{id}

### ViewListGroup (4 endpoints)
- [ ] GET /ViewListGroup
- [ ] POST /ViewListGroup
- [ ] DELETE /ViewListGroup/{id}
- [ ] GET /ViewListGroup/{id}

### ViewLists (4 endpoints)
- [ ] GET /ViewLists
- [ ] POST /ViewLists
- [ ] DELETE /ViewLists/{id}
- [ ] GET /ViewLists/{id}

### Virima (1 endpoints)
- [ ] GET /Virima/Get

### VirimaDetails (4 endpoints)
- [ ] GET /VirimaDetails
- [ ] POST /VirimaDetails
- [ ] DELETE /VirimaDetails/{id}
- [ ] GET /VirimaDetails/{id}

### VirtualAgent (4 endpoints)
- [ ] GET /VirtualAgent
- [ ] POST /VirtualAgent
- [ ] DELETE /VirtualAgent/{id}
- [ ] GET /VirtualAgent/{id}

### Vorboss (1 endpoints)
- [ ] GET /Vorboss/Get

### Webhook (4 endpoints) ⭐ CORE
- [ ] GET /Webhook
- [ ] POST /Webhook
- [ ] DELETE /Webhook/{id}
- [ ] GET /Webhook/{id}

### WebhookEvent (3 endpoints)
- [ ] GET /WebhookEvent
- [ ] POST /WebhookEvent
- [ ] GET /WebhookEvent/{id}

### WebhookRepository (2 endpoints)
- [ ] GET /WebhookRepository
- [ ] GET /WebhookRepository/{id}

### WhatsApp (2 endpoints)
- [ ] GET /WhatsApp/Get/Data
- [ ] GET /WhatsApp/Get/ProcessedIds

### WordpressDetails (4 endpoints)
- [ ] GET /WordpressDetails
- [ ] POST /WordpressDetails
- [ ] DELETE /WordpressDetails/{id}
- [ ] GET /WordpressDetails/{id}

### WordpressOrgDetails (4 endpoints)
- [ ] GET /WordpressOrgDetails
- [ ] POST /WordpressOrgDetails
- [ ] DELETE /WordpressOrgDetails/{id}
- [ ] GET /WordpressOrgDetails/{id}

### Workday (4 endpoints) ⭐ CORE
- [ ] GET /Workday
- [ ] POST /Workday
- [ ] DELETE /Workday/{id}
- [ ] GET /Workday/{id}

### Workflow (4 endpoints)
- [ ] GET /Workflow
- [ ] POST /Workflow
- [ ] DELETE /Workflow/{id}
- [ ] GET /Workflow/{id}

### WorkflowTarget (4 endpoints)
- [ ] GET /WorkflowTarget
- [ ] POST /WorkflowTarget
- [ ] DELETE /WorkflowTarget/{id}
- [ ] GET /WorkflowTarget/{id}

### XeroDetails (4 endpoints)
- [ ] GET /XeroDetails
- [ ] POST /XeroDetails
- [ ] DELETE /XeroDetails/{id}
- [ ] GET /XeroDetails/{id}

### XtypeRole (1 endpoints)
- [ ] GET /XtypeRole

### Zendesk (1 endpoints)
- [ ] GET /Zendesk/Get

### Zoom (1 endpoints)
- [ ] POST /Zoom/Message

### azureadconnection (4 endpoints)
- [ ] GET /azureadconnection
- [ ] POST /azureadconnection
- [ ] DELETE /azureadconnection/{id}
- [ ] GET /azureadconnection/{id}

### azureadmapping (1 endpoints)
- [ ] GET /azureadmapping

### cspinvoice (4 endpoints)
- [ ] GET /cspinvoice
- [ ] POST /cspinvoice
- [ ] DELETE /cspinvoice/{id}
- [ ] GET /cspinvoice/{id}

### formattedemail (4 endpoints)
- [ ] GET /formattedemail
- [ ] POST /formattedemail
- [ ] DELETE /formattedemail/{id}
- [ ] GET /formattedemail/{id}

### incomingemail (5 endpoints)
- [ ] GET /incomingemail
- [ ] POST /incomingemail
- [ ] POST /incomingemail/AddToTicket
- [ ] DELETE /incomingemail/{id}
- [ ] GET /incomingemail/{id}

### itemsupplier (4 endpoints)
- [ ] GET /itemsupplier
- [ ] POST /itemsupplier
- [ ] DELETE /itemsupplier/{id}
- [ ] GET /itemsupplier/{id}

### mcp (3 endpoints)
- [ ] DELETE /mcp
- [ ] GET /mcp
- [ ] POST /mcp

### pagerdutymapping (1 endpoints)
- [ ] GET /pagerdutymapping

### workflowstep (1 endpoints)
- [ ] GET /workflowstep
