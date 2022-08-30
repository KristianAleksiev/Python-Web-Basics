from django import template

register = template.Library()


@register.inclusion_tag(filename="tags/employees.html")
def employees_list():
    return {
        "employees": ["Pesho", "Gosho", "Roki"]
    }
