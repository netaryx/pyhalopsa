"""Releases command."""

from .._resource_cmd import make_resource_app

app = make_resource_app(
    name="releases",
    resource_attr="releases",
    list_columns=["id", "name", "releasetype_name", "product_name", "releasedate", "branch_name"],
    detail_columns=[
        "id", "name", "name_expanded", "releasetype_id", "releasetype_name",
        "branch_id", "branch_name", "builddate", "targetdate", "releasedate",
        "note", "public_note", "product_id", "product_name",
        "major_version_number", "minor_version_number", "patch_version_number",
    ],
)
