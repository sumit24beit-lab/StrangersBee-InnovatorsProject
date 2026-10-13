from django.shortcuts import render, get_object_or_404
from .models import HomeCook
from foodapp.models import Menu

# Create your views here.
def home_cooks_view(request):
    cooks = HomeCook.objects.filter(
        is_verified=True
    ).order_by('kitchen_name')
    return render(request, 'home_cooks/home_cooks.html', {'cooks': cooks})

def cook_profile_view(request, cook_id=None):
    if cook_id is None:
        return render(request, 'home_cooks/cook_profile.html')
    cook = get_object_or_404(HomeCook, pk=cook_id, is_verified=True)
    return render(request, 'home_cooks/cook_profile.html', {'cook': cook})

def kitchen_details_view(request):
    return render(request, 'home_cooks/kitchen_details.html')

def cook_meals_view(request, cook_id=None):
    if cook_id is None:
        cook = None
        meals = Menu.objects.filter(
            available=True,
            home_cook__is_verified=True,
        ).select_related("home_cook").order_by("name")
    else:
        cook = get_object_or_404(
            HomeCook,
            pk=cook_id,
            is_verified=True,
        )
        meals=Menu.objects.filter(
            home_cook=cook,
            available=True,
        ).order_by("name")
    return render(
        request, 
        'home_cooks/cook_meals.html',
        {
            "cook": cook,
            "meals": meals,
        },
    )

def meal_details_view(request, meal_id=None):
    if meal_id is None:
        return render(
            request,
            "home_cooks/meal_details.html"
        )
    meal = get_object_or_404(
        Menu.objects.select_related("home_cook"),
        pk=meal_id,
        available=True,
        home_cook__is_verified=True,
    )
    return render(
        request, 
        'home_cooks/meal_details.html',
        {"meal": meal},
    )

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