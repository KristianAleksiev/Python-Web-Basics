from django.shortcuts import render

from employees_app.employees.models import Department, Employee


# Create your views here.
def list_departments(request):
    context = {
        # "departments": Department.objects.all(),
        # "departments": Department.objects.filter(name__startswith="A", name__iendswith="p"),
        "departments": Department.objects.all(),
        "employees": Employee.objects.all()
    }

    return render(request, "list_departments.html", context)
