# FORM
class DeleteProfileForm(forms.ModelForm):
    # OVERWRITING SAVE
    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Profile
        exclude = ("first_name", "last_name", "picture", "email", "gender", "date_of_birth", "description")
        # or fields = ()


# VIEW
def profile_action(request, form_class, redirect_url, instance, template_name):
    if request.method == "POST":
        form = form_class(request.POST, instance=instance)
        if form.is_valid:
            form.save()
            return redirect(redirect_url)
    else:
        form = form_class(instance=instance)

    context = {
        "form": form,
    }
    return render(request, template_name, context)


def delete_profile(request):
    return render(request, DeleteProfileForm, "index", get_profile(), "profile_delete.html")