"""Reports command."""

from .._resource_cmd import make_resource_app

app = make_resource_app(
    name="reports",
    resource_attr="reports",
    list_columns=["id", "name", "charttype", "reportingperiod"],
    detail_columns=[
        "id", "name", "sql", "reportingperiod",
        "reportingperiodstartdate", "reportingperiodenddate",
        "charttitle", "charttype", "xaxis", "yaxis",
    ],
)
