import random

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy


# Create your views here.
def home(request):
    return HttpResponse("This is home")


def department(request):
    return HttpResponse("This is department")


def list_departments(request, id):
    return HttpResponse(f"This is department {id}")


def list_departments1(request):
    return HttpResponse("This is a list of departments 1")


def list_departments2(request):
    return HttpResponse("This is a list of departments 2")


def list_departments3(request):
    return HttpResponse("This is a list of departments 3")


def create_department(request):
    return HttpResponse("This is a CreateDepartment request")


def update_department(request):
    return HttpResponse("This is a UpdateDepartment request")


def delete_department(request):
    return HttpResponse("This is a DeleteDepartment request")


def redirect_to_home(request):
    print(reverse_lazy("create_department"))
    return redirect(to="create_department")


def template(request):
    random_number = random.randint(0, 1024)
    context = {
        "number": random_number,
    }
    return render(request, "index.html", context)