from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Restaurant
from django.views.generic import TemplateView

# Create your views here.
# in views.py

def about_page_view(request):
    return render(request, 'about.html')

def home_page_view(request):
    return render(request,'home.html')

def signup_view(request):
    return render(request,'signup.html')

def login_view(request):
    return render(request,'login.html')

def cart_view(request):
    return render(request,'cart.html')

def menu_view(request):
    return render(request,'menu.html')

def restaurant_view(request):
    return render(request,'restaurant.html')

def delivery_view(request):
    return render(request,'delivery.html')

def contact_view(request):
    return render(request,'contact.html')

def offers_view(request):
    return render(request,'offers.html')




