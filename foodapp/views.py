from django.http import HttpResponse
from django.shortcuts import render
from .models import Restaurant
from django.views.generic import TemplateView

# Create your views here.
# in views.py

def signup_page_view(request):
    return render(request,'signup.html')

def login_page_view(request):
    return render(request,'login.html')

def home_page_view(request):
    return render(request,'home.html')

def cart_page_view(request):
    return render(request,'cart.html')

def menu_page_view(request):
    return render(request,'menu.html')

def restaurant_page_view(request):
    return render(request,'restaurant.html')

def delivery_page_view(request):
    return render(request,'delivery.html')

def contact_page_view(request):
    return render(request,'contact.html')

def offers_page_view(request):
    return render(request,'offers.html')

def chatbot_page_view(request):
    return render(request,'chatbot.html')


