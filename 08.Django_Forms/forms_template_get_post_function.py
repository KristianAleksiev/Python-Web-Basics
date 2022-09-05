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


def create_profile(request):
    return profile_action(request, CreateProfileForm, "index", Profile(), "profile_create.html")


def edit_profile(request)
    return profile_action(request, EditProfileForm, "profile details", get_profile(), "profile_edit.html")
