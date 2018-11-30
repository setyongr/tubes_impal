from django import template

register = template.Library()


@register.inclusion_tag("table_lib/table.html")
def render_table(table):
    return {
        "table": table
    }
