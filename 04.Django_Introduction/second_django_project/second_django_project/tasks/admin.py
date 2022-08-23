from django.contrib import admin

from second_django_project.tasks.models import Task

# Register your models here.
# First variant in admin.py
# admin.site.register(Task)
# Second variant in admin.py

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    pass
