from django.http import HttpResponse
from django.shortcuts import render
from second_django_project.tasks.models import Task

# Create your views here.

# def home(request):
#     html = """
#     <h1> It works! </h1>
#     <ul>
#         <l1> 1 </li>
#         <l1> 2 </li>
#         <l1> 3 </li>
#         <l1> 4 </li>
#     </ul>
#     """
#     return HttpResponse(html)


def home(request):
    context = {
        "title": "It works from view!",
        "tasks": Task.objects.all(),
    }
    return render(request, "home.html", context)