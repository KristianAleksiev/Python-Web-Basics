from django.apps import AppConfig

from employees_app import employees


class EmployeesConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "employees_app.employees"
