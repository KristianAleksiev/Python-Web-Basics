"""
1. Django Templates
- Python string marked-up using the Django template language
- Django defines a standard API for loading and rendering templates regardless of the backend
- Preprocessing the identifier's template
- Dynamically generated HTML
- Server-side rendering

Blocks of DTL:
- Variables :
-- surrounded by {{ variable }}
-- Inside the context -> ".", " " cannot be included in the key, cannot start with a number, "_"

- Filters
-- Can be chained
-- Achieved by pipe symbol

<h2>{{ title|lower }}:</h2>  - |lower, |capfirst, |truncatewords:, |truncatechars:, |join:
<p>{{ description|truncatewords:10 }}</p>
<li>{{ employees|join:', ' }}</li>

- Tags
-- Function which returns a value to be displayed
{% if, else, %} X {% endif %}

-- Logic is executed in the views
-- csrf_token Tag -> something unique that's changing on every request (Security)
<div>
    {{ csrf_token }}
</div>

---------------------------------------------

2. Custom filters
- Create package -> templatetags
--
from django import template
register = template.Library()
@register.filter(name="capitalize")
--
def capitalize(value: str):
    return value[0].upper() + value[1:].lower()

---------------------------------------------

3. Custom tags

from django import template
register = template.Library()
@register.inclusion_tag(filename="tags/employees.html")  <====
def employees_list():
    return {
        "employees": ["Pesho", "Gosho", "Roki"]
    }

---------------------------------------------

4. Template inheritance
- Important - Naming the block
templates/base/base.html =>
{%base NAME%}
Base template
{% endbase %}

{% extends "base/base.html" %}
 {% block NAME(NAME OF THE BLOCK IN THE BASE) %} => The current html page is extending parent "base"
 {% endblock %}

HTML BACKBONE IN THE PARENT, ONLY DIFFERENT TAGS IN THE CHILD
---------------------------------------------

5. Static files - (js, css, images etc.)
SETTINGS.py -> Static
STATICFILES_DIRS = [
BASE_DIR / "staticfiles",
]
staticfiles folder on manage.py level

<link rel="stylesheet" href="{% static "main.css" %}">
"""
