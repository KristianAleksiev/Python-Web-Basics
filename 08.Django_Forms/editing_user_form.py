def edit_profile(request):
    profile = get_profile()

    if request.method == "POST":
        form = ProfileForm(request.POST, instance=profile)

        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = ProfileForm()

    context = {
        "form": form,
    }
    return render(request, "profile_edit.html", context)