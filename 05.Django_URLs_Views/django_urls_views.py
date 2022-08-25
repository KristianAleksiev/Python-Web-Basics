"""
URLS
1. Mapping the http requests to a specific view
A function is Django view if:
- Accepts request as first param
- Returns HttpResponse object

-------------------------------------

2. Calls the given view and passes it an instance of the HttpRequest

-------------------------------------

3. URL to view, urlpatterns variable => tuple or list

-------------------------------------

4. Managing request address => path("x", WhatToSendBack)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home),  # "localhost:8000" -> home
    path("department/", department),  # "localhost:8000/department/ -> department"
    path("department/2/", home),  # "localhost:8000/department/ -> home"
    #  PATH => VIEW - URLS -> VIEWS
                        Function based / Class based
Always with / at end of url, APPEND_SLASH Setting

-------------------------------------

5. Creating urls.py inside the app folder, -> Easier to track and debug, INCLUDING it into the project urls so it:
- Avoids repetition, easier debugging, abstract
    path("departments/create/", create_department),
    path("departments/update/", update_department),
    path("departments/delete/", delete_department), ==>>>>

    path("departments/", include("app.urls") - INSIDE PROJECT URLS

    urlpatterns = [                          - INSIDE APP URLS
    path("create/", create_department),
    path("update/", update_department),
    path("delete/", delete_department),

]

Dynamic URLS
    path("1/", list_departments1),
    path("2/", list_departments2),
    path("3/", list_departments3),

    path(<id>/, list_departments)

    Type could be specified:
    path(<int:id>/, list_departments)


in Views :
def list_departments(request, id): <=======
    return HttpResponse(f"This is department {id}")

-------------------------------------

Class based Views:
    Class HomeView(TemplateView):
        template_name = "index.html"

-------------------------------------

Responses:
    def home(request):
        if request.method == "POST":
            return HttpResponse(f"{request.method}: This is home", status=201, headers={"x-header": "Django"})
        else:
            return HttpResponse(f"{request.method}: This is home")

-------------------------------------

Django Shortcut Functions:
1. Redirect
def redirect_to_home(request):
    return redirect(to="/")  301, response headers - location

2. Render
def template(request):
    return render(request, "index.html", content_type="text/plain") <= Could be modified

With context:
def template(request):
    random_number = random.randint(0, 1024)
    context = {
        "number": random_number,
    }
    return render(request, "index.html", context)

"""
