from django.contrib import admin

from employees_app.employees.models import Employee, Department


# # Register your models here.
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("id", "first_name", "last_name", "company", "job_title")


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    pass


