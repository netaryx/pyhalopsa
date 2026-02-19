"""Items command."""

from .._resource_cmd import make_resource_app

app = make_resource_app(
    name="items",
    resource_attr="items",
    list_columns=["id", "name", "assetgroup_name", "baseprice", "quantity_in_stock", "status"],
    detail_columns=[
        "id", "name", "status", "assetgroup_id", "assetgroup_name", "note",
        "supplier_part_code", "description", "purchase_description",
        "quantity_in_stock", "quantity_reserved", "quantity_on_order",
        "baseprice", "supplier_id", "supplier_name",
        "manufacturer_id", "manufacturer_name", "type",
    ],
)
