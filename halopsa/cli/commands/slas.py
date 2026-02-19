"""SLAs command."""

from .._resource_cmd import make_resource_app

app = make_resource_app(
    name="slas",
    resource_attr="slas",
    list_columns=["id", "name", "workday_id"],
    detail_columns=[
        "id", "name", "workday_id", "responsereset", "autoreleaseoption",
    ],
)
