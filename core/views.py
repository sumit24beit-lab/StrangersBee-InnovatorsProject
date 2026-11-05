from django.shortcuts import render

# Create your views here.
def landing_page_view(request):
    return render(request, "core/landing.html")

def about_page_view(request):
    return render(request, "core/about.html")
