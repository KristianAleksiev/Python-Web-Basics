class EmployeeForm(forms.ModelForm):
    class Meta:  # <=======
        model = Employee  # (MODEL)
        # fields = ("first_name", "last_name", "egn")
        fields = "__all__"
        widgets = {
            "first_name": forms.TextInput(
                attrs={"class": "form-control"}
            )
        }


def create_employee(request):
    if request.method == "POST":
        employee_form = EmployeeForm(request.POST)

        if employee_form.is_valid():
            employee_form.save()
            return redirect("home page")

    employee_form = EmployeeForm()

    context = {
        "employee_form": employee_form,
        "employees": Employee.objects.all(),
    }
    return render(request, "create.html", context)
