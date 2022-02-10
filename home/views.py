from django.shortcuts import render

# Create your views here.
#everybody can see this page.
def homepage(request):
    return render(request, "home.html")