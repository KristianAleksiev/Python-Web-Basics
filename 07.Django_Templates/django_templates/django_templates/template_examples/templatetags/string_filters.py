from django import template

register = template.Library()


@register.filter(name="capitalize")
def capitalize(value: str):
    """Capitalizes the value, i.e. makes the first letter capital"""

    return value[0].upper() + value[1:].lower()
