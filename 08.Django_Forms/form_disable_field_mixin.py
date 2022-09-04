# Single field
class DisableFieldsFormMixin:
    disabled_fields = ()
    fields = {}

    def _init_disabled_fields(self):
        for _, field in self.fields.items():
            if not hasattr(field.widget, "attrs"):
                setattr(field.widget, "attrs", {})
            field.widget.attrs["readonly"] = "readonly"




class DeletePetForm(BootstrapFormMixin, forms.ModelForm, DisableFieldsFormMixin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()
        self._init_disabled_fields()

    class Meta:
        model = Pet
        exclude = ("user_profile",)


# ALL FIELDS
class DisableFieldsFormMixin:
    disabled_fields = "__all__"
    fields = {}

    def _init_disabled_fields(self):
        for name, field in self.fields.items():
            if self.disabled_fields !="all" and name not in self.disabled_fields:
                continue
            if not hasattr(field.widget, "attrs"):
                setattr(field.widget, "attrs", {})
            field.widget.attrs["readonly"] = "readonly"


class DeletePetForm(BootstrapFormMixin, forms.ModelForm, DisableFieldsFormMixin):
    disabled_fields = ("name", )  # <========================= If a single field need to be disabled
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()
        self._init_disabled_fields()

    class Meta:
        model = Pet
        exclude = ("user_profile",)