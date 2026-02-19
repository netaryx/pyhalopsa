"""Categories command."""

from .._resource_cmd import make_resource_app

app = make_resource_app(
    name="categories",
    resource_attr="categories",
    list_columns=["id", "value", "category_name", "type_id", "inactive"],
    detail_columns=[
        "id", "value", "category_name", "type_id", "sla_id",
        "priority_id", "chargerate", "category_group_id", "sequence", "inactive",
    ],
)
