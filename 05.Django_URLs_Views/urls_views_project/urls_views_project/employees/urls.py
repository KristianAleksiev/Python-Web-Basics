from django.urls import path

from urls_views_project.employees.views import create_department, update_department, delete_department, \
    list_departments1, list_departments2, list_departments3, redirect_to_home

urlpatterns = [
    path("create/", create_department, name="create_department"),
    path("update/", update_department),
    path("delete/", delete_department),
    path("1/", list_departments1),
    path("2/", list_departments2),
    path("3/", list_departments3),


]
