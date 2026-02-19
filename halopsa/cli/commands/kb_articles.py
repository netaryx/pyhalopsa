"""Knowledge base articles command."""

from .._resource_cmd import make_resource_app

app = make_resource_app(
    name="kb-articles",
    resource_attr="kb_articles",
    list_columns=["id", "name", "view_count", "date_created", "date_edited", "type", "inactive"],
    detail_columns=[
        "id", "name", "description", "view_count", "useful_count", "notuseful_count",
        "date_created", "date_edited", "tag_string", "inactive", "type",
        "next_review_date", "creator_id", "creator_name",
        "editor_id", "editor_name", "link",
    ],
)
