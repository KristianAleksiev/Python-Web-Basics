from django.urls import path
from second_django_project.tasks.views import home

urlpatterns = (
    path("", home),
)
