class BootstrapFormMixin:
    # FIELDS DICT
    fields = {}

    def _init_bootstrap_form_controls(self):
        for _, field in self.fields.items():
            if not hasattr(field.widget, "attrs"):
                setattr(field.widget, "attrs", {})

            if "class" not in field.widget.attrs:
                field.widget.attrs["class"] = ""

            field.widget.attrs["class"] += "form-control"


class ProfileForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    class Meta:
        model = Profile
        fields = ("first_name", "last_name", "picture")
        widgets = {
            # "first_name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter first name"}),
            # "last_name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter last name"}),
            # "picture": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter URL"}),
            "first_name": forms.TextInput(attrs={"placeholder": "Enter first name"}),
            "last_name": forms.TextInput(attrs={"placeholder": "Enter last name"}),
            "picture": forms.TextInput(attrs={"placeholder": "Enter URL"}),
        }