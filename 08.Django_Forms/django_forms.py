"""
1. Django forms

- Used for Client information input which is send back to the server
- We specify in what format does the user provide the information
- The only HTTP methods used in forms are GET and POST
- Forms are two types:
Bound - Capable of validating data and rendering the form as HTML with the data displayed (Django Form)
Unbound - Cannot do validations (Pure HTML Form)

- Generating HTML from widgets in Django forms
- Validate data and process it into a Python data structure
- Creating form versions of Django Models
- Quick update of Models from Forms

Executed in VIEWS
from django import forms

class FormName(forms.Form):
    name = forms.CharField(max_length=50,)
    age = forms.IntegerField()


HTML file
    <form action="{% url 'create employee' %}"> <===== Name of the view
        {{ employee_form }}
        <button>Save</button>   <===== Mandatory (<input type="submit" value="Save" />
    </form>

def create_employee(request):
    print(request.GET) or (request.POST) depending on the form method <=== The Information from the client
    pass
2. Built-in widgets
- Overriding the defaults

- widget={"input_type": "text}
- widget={"input_type": "number"}
- widget={"input_type": "password"}
- widget={"input_type": "email"}
- widget={"input_type": "url"}
- widget={"input_type": "email"}
- .........
-
3. Validation Forms
- A function with EXACTLY 1 param again.
- Built-in / Custom

4. Django ModelForm class
- Used in database-driven apps, the form overlaps the Model
- ModelForm helper class, defining the fields and the types is skipped (defined in the model)

-class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee  # (MODEL)
        # fields = ("first_name", "last_name", "egn")
        fields = "__all__"

5. Validating Model Forms
6. Bots and Bot catchers
- csrf_token -> The client which made a GET, made a POST
- need to be added {% crsf_token %} tag in the forms
DTL
    <form method="POST" action="{% url 'create employee' %}">
        {{ employee_form }}
            {% crsf_token %}
        <button>Save</button>
    </form>

VIEW
class EmployeeForm(forms.ModelForm):
    bot_catcher = forms.CharField(
        widget=forms.HiddenInput(),
        )

    def clean_bot_catcher(self)
        value = self.cleaned_data["bot_catcher"]
        if value:
            raise ValidationError("This is a web crawler")

7. Media Files - Pillow
- User uploaded
In Models
# Create your models here.
class Employee(models.Model):
    image = models.ImageField(
        null=True,
        blan=True,
        upload_to="profiles"
    )

In the Form:
def create_employee(request):
    if request.method == "POST":
        employee_form = EmployeeForm(request.POST, request.FILES) <========

enctype="multipart/form-data" INSIDE THE FORM

URLS ->
+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
"""
