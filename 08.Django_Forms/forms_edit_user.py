#FORM
class EditProfileForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()


    class Meta:
        model = Profile
        fields = "__all__"
        widgets = {
            "first_name": forms.TextInput(attrs={"placeholder": "Enter first name"}),
            "last_name": forms.TextInput(attrs={"placeholder": "Enter last name"}),
            "picture": forms.TextInput(attrs={"placeholder": "Enter URL"}),
            "email": forms.EmailInput(attrs={"placeholder": "Email"}),
            "description": forms.Textarea(attrs={"placeholder": "Enter description", "rows": 3, }),
            "date_of_birth": forms.DateInput(attrs={"min": "1920-01-01"}),
        }

#VIEW
def edit_profile(request):
    profile = get_profile()

    if request.method == "POST":
        form = EditProfileForm(request.POST, instance=profile)

        if form.is_valid():
            form.save()
            return redirect("profile details")
    else:
        form = EditProfileForm(instance=profile)

    context = {
        "form": form,
    }
    return render(request, "profile_edit.html", context)