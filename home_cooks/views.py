from django.shortcuts import render

# Create your views here.
def home_cooks_view(request):
    return render(request, 'home_cooks/home_cooks.html')

def cook_profile_view(request):
    return render(request, 'home_cooks/cook_profile.html')

def kitchen_details_view(request):
    return render(request, 'home_cooks/kitchen_details.html')

def cook_meals_view(request):
    return render(request, 'home_cooks/cook_meals.html')

def meal_details_view(request):
    return render(request, 'home_cooks/meal_details.html')

def dashboard_view(request):
    return render(request, 'home_cooks/dashboard.html')

def my_profile_view(request):
    return render(request, 'home_cooks/my_profile.html')

def my_meals_view(request):
    return render(request, 'home_cooks/my_meals.html')

def cook_orders_view(request):
    return render(request, 'home_cooks/cook_orders.html')

def cook_earnings_view(request):
    return render(request, 'home_cooks/cook_earnings.html')