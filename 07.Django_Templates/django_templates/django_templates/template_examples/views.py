from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, "localhost_template.html")


def index(request):
    context = {
        "title": "Employees list",
        # "employees": Employee.objects.all()
        "employees": ["Gogo", "Maria", "Stefan", "Cvetanka"],
        "description": "Lorem ipsum dolor sit amet, consectetur adipisicing elit.",
        "first_number": 123,
        "second_number": 321,
        "numbers": [123, 321, 200, 555],
    }
    context["numbers"].sort()
    return render(request, "templates_examples.html", context)
