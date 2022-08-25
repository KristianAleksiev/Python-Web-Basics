"""urls_views_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from . import employees
from .employees.views import home, department, list_departments, redirect_to_home, template

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("urls_views_project.employees.urls")),  # "localhost:8000" -> home
    # path("departments/", list_departments),  # "localhost:8000/department/ -> department"
    # path("departments/2/", department),  # "localhost:8000/department/ -> home"
    # #  PATH => VIEW
    # path("go-to-home/", redirect_to_home, name="home"),
    path("template/", template)
]
