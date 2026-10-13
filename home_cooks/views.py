from django.shortcuts import render, get_object_or_404, redirect
from .models import HomeCook
from foodapp.models import Menu
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import HomeCookForm, MenuForm
from django.views.decorators.http import require_POST

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

@login_required(login_url="login")
def my_profile_view(request):
    profile = HomeCook.objects.filter(user=request.user).first()
    if request.method == "POST":
        form = HomeCookForm(request.POST, instance=profile,)
        if form.is_valid():
            profile = form.save(commit=False)
            if profile.pk is None:
                profile.user = request.user
            profile.save()
            messages.success(request, "Your kitchen profile has been saved successfully.",)
            return redirect("my_profile")
    else:
        form = HomeCookForm(instance=profile)
    return render(
        request,
        'home_cooks/my_profile.html',
        {
            "form": form,
            "profile": profile,
        },
    )

@login_required(login_url="login")
def my_meals_view(request):
    cook = HomeCook.objects.filter(
        user=request.user
    ).first()
    if cook is None:
        messages.warning(request, "Please complete your home cook profile first.",)
        return redirect("my_profile")
    meals = Menu.objects.filter(home_cook=cook).order_by("name")
    return render(
        request,
        'home_cooks/my_meals.html',
        {
            "cook": cook,
            "meals": meals,
            "total_meals": meals.count(),
            "available_meals": meals.filter(available=True).count(),
            "unavailable_meals": meals.filter(available=False).count(),
        },
    )

@login_required(login_url="login")
def add_meal_view(request):
    cook = HomeCook.objects.filter(user=request.user).first()
    if cook is None:
        messages.warning(request, "Please complete your home cook profile first.",)
        return redirect("my_profile")
    if request.method == "POST":
        form = MenuForm(request.POST, request.FILES,)
        if form.is_valid():
            meal = form.save(commit=False)
            meal.home_cook = cook
            meal.save()
            messages.success(request, "Your meal has been added successfully.",)
            return redirect("my_meals")
    else:
        form = MenuForm()
    return render(
        request,
        "home_cooks/meal_form.html",
        {
            "form": form,
            "page_title": "Add New Meal",
        },
    )

@login_required(login_url="login")
def edit_meal_view(request, meal_id):
    cook = HomeCook.objects.filter(user=request.user).first()
    if cook is None:
        messages.warning(request, "Please complete your home cook profile first.",)
        return redirect("my_profile")
    meal = get_object_or_404(Menu, pk=meal_id, home_cook=cook,)
    if request.method == "POST":
        form = MenuForm(request.POST, request.FILES, instance=meal,)
        if form.is_valid():
            form.save()
            messages.success(request, "Your meal has been updated successfully.",)
            return redirect("my_meals")
    else:
        form = MenuForm(instance=meal)
    return render(
        request,
        "home_cooks/meal_form.html",
        {
            "form": form,
            "page_title": "Edit Meal",
            "meal": meal,
        },
    )

@login_required(login_url="login")
@require_POST
def toggle_meal_availability_view(request, meal_id):
    cook = HomeCook.objects.filter(
        user=request.user
    ).first()
    if cook is None:
        messages.warning(
            request,
            "Please complete your home cook profile first.",
        )
        return redirect("my_profile")
    meal = get_object_or_404(
        Menu,
        pk=meal_id,
        home_cook=cook,
    )
    meal.available = not meal.available
    meal.save(update_fields=["available"])
    if meal.available:
        messages.success(
            request,
            f"{meal.name} is now available for orders.",
        )
    else:
        messages.success(
            request,
            f"{meal.name} is now unavailable for orders.",
        )
    return redirect("my_meals")


def cook_orders_view(request):
    return render(request, 'home_cooks/cook_orders.html')

def cook_earnings_view(request):
    return render(request, 'home_cooks/cook_earnings.html')
