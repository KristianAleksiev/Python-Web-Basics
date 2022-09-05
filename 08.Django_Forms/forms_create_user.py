# FORM
class CreateProfileForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()
        self.initial["gender"] = Profile.DO_NOT_SHOW

    class Meta:
        model = Profile
        fields = ("first_name", "last_name", "picture")
        widgets = {
            "first_name": forms.TextInput(attrs={"placeholder": "Enter first name"}),
            "last_name": forms.TextInput(attrs={"placeholder": "Enter last name"}),
            "picture": forms.TextInput(attrs={"placeholder": "Enter URL"}),
        }


# VIEW

def create_profile(request):
    if request.method == "POST":
        # Create a form with POST
        form = CreateProfileForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("index")

    else:
        # Create empty form
        form = CreateProfileForm()

    context = {
        "form": form,
    }
    return render(request, "profile_create.html", context)
