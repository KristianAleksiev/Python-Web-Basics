from django.urls import path

from django_templates.template_examples.views import index

urlpatterns = [
    path("templates/", index, name="templates index")
]