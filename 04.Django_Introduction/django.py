"""
1. What is Django?
- Web framework
- Provides a foundation on which software developers can build programs for a specific platform
- Includes an API
- Manages the HTTP communication
- Ability to work with databases based on OOP
- Abstraction on creating web applications
- High-level, fast, secure, scalable, free and open source
- Architecture pattern - MTV - Model-Template-View (MVC, MVVM, MTV, MVP)
Data - Presentation - Logic

------------------------------------------------------------

2. Creating a Django project
- __init__ - Python package
- asgi.py -
- settings.py - Django Project config
- urls.py - Table of content
- wsgi.py -
- manage.py - Command executing - makemigrations, startapp, migrate
python manage.py runserver

A project can contain multiple apps

------------------------------------------------------------

3. Creating a Django App
- Does something (login, logout, profiles etc...)
- Can be in multiple projects theoretically
python manage.py startapp task

admin.py - Django admin site, not django-admin
models.py -

views.py - requests
- Function based views
- CLass based views

Each view should be routed => Where does it get the request

------------------------------------------------------------

4. Setting up a database
python manage.py migrate

Code-first approach:

class Task(models.Model):
    title = models.CharField(
        max_length=15,
        null=False,
        unique=True,

    )
    text = models.CharField(
        max_length=50,
    )
python manage.py makemigrations => INSTALLED APPS
python manage.py migrate
python manage.py inspectdb => From table generates Classes

------------------------------------------------------------

5. Writing a simple task app
items = Task.objects.all() => Query set

------------------------------------------------------------

6. Django Admin Site
- Automatic admin interface
- Automatic migrations of models

python manage.py createsuperuser

Registering models in admin panel:

- First variant in admin.py
admin.site.register(Task)

- Second variant in admin.py
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    pass

------------------------------------------------------------

7. Templates
- Generate HTML dynamically
- Static parts of the HTML output and special syntax
- Django Templates / Jinja2

- In order to render from view => Needs to be injected into the home.html as follows
VIEW:
def home(request):
    context = {
        "title": "It works from view!"
    }
    return render(request, "home.html", context)

HOME.HTML:
<h1>{{ title }}</h1>


Injecting dynamically into the HTML:
VIEW:
 context = {
        "title": "It works from view!",
        "tasks": Task.objects.all(),
HOME.HTML:
<ul>
    {% for task in tasks %}
        <li>{{ task.title }}</li>
    {% endfor %}
</ul>

DJANGO TEMPLATE LANGUAGE
------------------------------------------------------------

Client => URL => Django => VIEW => render(template, context) => Django translate to HTML => Response
"""