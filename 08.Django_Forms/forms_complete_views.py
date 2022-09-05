# Without optimizations
"""
def create_employee(request):
    if request.method == "GET":
        context = {
            "employee_form": EmployeeForm(),  # As instance
        }
        return render(request, "create.html", context)
    else:
        employee_form = EmployeeForm(request.POST)  # As instance with request body
        if employee_form.is_valid():
            return redirect("home page")

        context = {
            "employee_form": EmployeeForm,  # The one created above if it doesn't pass the validations
        }
        return render(request, "create.html", context)
"""


# Optimized
def create_employee(request):
    if request.method == "POST":
        employee_form = EmployeeForm(request.POST)

        if employee_form.is_valid():
            return redirect("home page")

    employee_form = EmployeeForm()

    context = {
        "employee_form": employee_form,
    }
    return render(request, "create.html", context)


# Adding the data from the form to the database (Variant 1):

def create_employee(request):
    if request.method == "POST":
        employee_form = EmployeeForm(request.POST)

        #  Each passed validation gets added to "cleaned_data", so  we get it from there
        if employee_form.is_valid():

            emp = Employee(
                first_name=employee_form.cleaned_data["first_name"],
                last_name=employee_form.cleaned_data["last_name"],
                job_title=employee_form.cleaned_data["job_title"],
                egn=employee_form.cleaned_data["egn"],
                company=employee_form.cleaned_data["company"],
            )
            # emp = Employee(**employee_form.cleaned_data, department_id=1)

            emp.full_clean()  # <=== Explicit call of validators
            emp.save()

            return redirect("home page")

    employee_form = EmployeeForm()

    context = {
        "employee_form": employee_form,
    }
    return render(request, "create.html", context)


# ModelForm Class regarding Data-Driven Apps