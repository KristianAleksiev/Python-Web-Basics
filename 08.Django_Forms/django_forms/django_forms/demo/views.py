from django import forms
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect

from django_forms.demo.models import Employee


class EmployeeForm(forms.Form):
    first_name = forms.CharField(max_length=40, label="Enter your first name")
    last_name = forms.CharField(max_length=40, )
    age = forms.IntegerField(widget=forms.TextInput(attrs={"type": "range"}))
    password = forms.CharField(widget=forms.PasswordInput, )
    birthday = forms.DateTimeInput()
    sender = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)


class EmployeeFormTwo(forms.ModelForm):
    bot_catcher = forms.CharField(
        widget=forms.HiddenInput(),
        required=False,
    )

    def clean_bot_catcher(self)
        value = self.cleaned_data["bot_catcher"]
        if value:
            raise ValidationError("This is a web crawler")


    class Meta:
        model = Employee
        fields="__all__"

def home(request):
    return render(request, "forms_demo.html")


# def create_employee(request):
#     if request.method == "POST":
#         employee_form = EmployeeForm(request.POST)
#
#         if employee_form.is_valid():
#             emp = Employee(
#                 first_name=employee_form.cleaned_data["first_name"],
#                 last_name=employee_form.cleaned_data["last_name"],
#                 job_title=employee_form.cleaned_data["job_title"],
#                 egn=employee_form.cleaned_data["egn"],
#                 company=employee_form.cleaned_data["company"],
#             )
#             # emp = Employee(**employee_form.cleaned_data, department_id=1)
#             emp.save()
#
#             return redirect("home page")
#
#     employee_form = EmployeeForm()
#
#     context = {
#         "employee_form": employee_form,
#     }
#     return render(request, "create.html", context)
def create_employee(request):
    if request.method == "POST":
        employee_form = EmployeeForm(request.POST, request.FILES)

        if employee_form.is_valid():
            employee_form.save()
            return redirect("home page")

    employee_form = EmployeeForm()

    context = {
        "employee_form": employee_form,
        "employees": Employee.objects.all(),
    }
    return render(request, "create.html", context)
