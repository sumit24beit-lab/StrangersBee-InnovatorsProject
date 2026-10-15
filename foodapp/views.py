import json
import re

from django.db import transaction
from django.http import HttpResponse, JsonResponse
from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404
from .models import (
    Address, 
    CustomerProfile, 
    Menu, 
    Order,
    OrderItem,
)
from django.views.generic import TemplateView
from .decorators import customer_required
from django.contrib import messages
from .forms import CustomerProfileForm, AddressForm
from django.views.decorators.http import require_POST

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

@customer_required
def cart_view(request):
    return render(request,'cart.html')

def menu_view(request):
    meals = (
        Menu.objects.filter(
            available=True,
            home_cook__is_verified=True,
        )
        .select_related("home_cook")
        .order_by("name")
    )
    meals_data = [
        {
            "id": meal.pk,
            "name": meal.name,
            "restaurant": meal.home_cook.kitchen_name,
            "cuisine": meal.home_cook.get_specialty_cuisine_display(),
            "price": float(meal.price),
            "calories": 0,
            "nutrients": meal.nutrients,
            "ingredients": meal.ingredients or meal.description,
            "img": (
                meal.image.url
                if meal.image
                else "/static/foodapp/images/food5.jpg"
            ),
            "nutri": meal.nutrient_function,
            "meal": meal.meal_time,
            "type": meal.food_type,
            "spice": meal.spice_level,
        }
        for meal in meals
    ]
    return render(
        request,
        'menu.html',
        {
            'meals': meals,
            'meals_data': meals_data,
        },
    )

def restaurant_view(request):
    return render(request,'restaurant.html')

@customer_required
def delivery_view(request):
    profile = get_or_create_customer_profile(request.user)
    addresses = profile.customer_addresses.order_by(
        "-created_at_date"
    )
    return render(
        request,
        'delivery.html',
        {
            "profile": profile,
            "addresses": addresses,
        },
    )

def contact_view(request):
    return render(request,'contact.html')

def offers_view(request):
    return render(request,'offers.html')

@customer_required
def customer_profile_view(request):
    profile, created = CustomerProfile.objects.get_or_create(
        user=request.user.username,
        defaults={
            "first_name": request.user.first_name,
            "last_name": request.user.last_name,
            "email": request.user.email,
        },
    )
    if request.method == "POST":
        form = CustomerProfileForm(
            request.POST,
            instance=profile,
        )
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user.username
            profile.email = request.user.email
            profile.save()
            messages.success(
                request,
                "Your profile has been updated successfully.",
            )
            return redirect("customer_profile")
    else:
        form = CustomerProfileForm(instance=profile)
    return render(
        request,
        "customer_profile.html",
        {
            "form": form,
            "profile": profile,
        },
    )

@customer_required
def customer_addresses_view(request):
    profile = get_or_create_customer_profile(request.user)
    addresses = profile.customer_addresses.order_by("-created_at_date")
    return render(
        request,
        "customer_addresses.html",
        {
            "profile": profile,
            "addresses": addresses,
        },
    )

@customer_required
def customer_address_add_view(request):
    profile = get_or_create_customer_profile(request.user)
    if request.method == "POST":
        form = AddressForm(request.POST)
        if form.is_valid():
            address = form.save(commit=False)
            address.customer = profile
            address.save()
            messages.success(
                request,
                "Address added successfully.",
            )
            return redirect("customer_addresses")
    else:
        form = AddressForm()
    return render(
        request,
        "address_form.html",
        {
            "form": form,
            "page_title": "Add Address",
        },
    )

@customer_required
def customer_address_edit_view(request, address_id):
    profile = get_or_create_customer_profile(request.user)
    address = get_object_or_404(
        Address,
        pk=address_id,
        customer=profile,
    )
    if request.method == "POST":
        form = AddressForm(
            request.POST,
            instance=address,
        )
        if form.is_valid():
            form.save()
            messages.success(
                request,
                "Address updated successfully",
            )
            return redirect("customer_addresses")
    else:
        form = AddressForm(instance=address)
    return render(
        request,
        "address_form.html",
        {
            "form": form,
            "page_title": "Edit Address",
        },
    )

@customer_required
@require_POST
def customer_address_delete_view(request, address_id):
    profile = get_or_create_customer_profile(request.user)
    address = get_object_or_404(
        Address,
        pk=address_id,
        customer=profile,
    )
    address.delete()
    messages.success(
        request,
        "Address deleted successfully.",
    )
    return redirect("customer_addresses")

def get_or_create_customer_profile(user):
    profile = CustomerProfile.objects.filter(
        user=user.username
    ).first()
    if profile is None:
        profile = CustomerProfile.objects.create(
            user=user.username,
            first_name=user.first_name,
            last_name=user.last_name,
            email=user.email,
        )
    return profile

@customer_required
def order_history_view(request):
    customer_profile = CustomerProfile.objects.filter(
        user=request.user.username
    ).first()
    if customer_profile is None:
        orders = Order.objects.none()
    else:
        orders = (
            Order.objects
            .filter(customer=customer_profile)
            .select_related("address")
            .prefetch_related("items__menu_item__home_cook")
            .order_by("-created_at")
        )
    return render(
        request,
        "order_history.html",
        {
            "orders": orders,
        },
    )

@customer_required
@require_POST
def place_order_view(request):
    try:
        data = json.loads(request.body or "{}")
    except (json.JSONDecodeError, UnicodeDecodeError):
        return JsonResponse(
            {"error": "Invalid request data."},
            status=400,
        )
    if not isinstance(data, dict):
        return JsonResponse(
            {"error": "Invalid request data."},
            status=400,
        )
    if data.get("payment_method") != "cod":
        return JsonResponse(
            {
                "error": (
                    "Online payment is not available yet. "
                    "Please select Cash on Delivery."
                )
            },
            status=400,
        )
    phone = str(data.get("phone", "")).strip()
    digits = re.sub(r"\D", "", phone)
    # Accept either a 10-digit Indian number of +91 followed by 10 digits.
    if len(digits) == 12 and digits.startswith("91"):
        digits = digits[2:]
    if not re.fullmatch(r"[6-9]\d{9}", digits):
        return JsonResponse(
            {
                "error": "Enter a valid 10-digit mobile number."
            },
            status=400,
        )
    raw_address_id = data.get("address_id")
    raw_items = data.get("items")
    try:
        address_id = int(raw_address_id)
    except (TypeError, ValueError):
        return JsonResponse(
            {"error": "Please select a saved delivery address."},
            status=400,
        )
    if not isinstance(raw_items, list) or not raw_items:
        return JsonResponse(
            {"error": "Your cart is empty."},
            status=400,
        )
    # Validate item IDs and quantities. Never trust client-side prices.
    quantities = {}
    for item in raw_items:
        if not isinstance(item, dict):
            return JsonResponse(
                {"error": "Invalid cart item."},
                status=400,
            )
        try:
            menu_id = int(item.get("id"))
            quantity = int(item.get("qty"))
        except (TypeError, ValueError):
            return JsonResponse(
                {"error": "Invalid menu item or quantity."},
                status=400,
            )
        if menu_id <= 0 or quantity <= 0:
            return JsonResponse(
                {"error": "Invalid menu item or quantity."},
                status=400,
            )
        quantities[menu_id] = quantities.get(menu_id, 0) + quantity
        if quantities[menu_id] > 99:
            return JsonResponse(
                {"error": "Maximum quantity per meal is 99."},
                status=400,
            )
    profile = get_or_create_customer_profile(request.user)
    address = Address.objects.filter(
        pk=address_id,
        customer=profile,
    ).first()
    if address is None:
        return JsonResponse(
            {"error": "The selected delivery address is invalid."},
            status=400,
        )
    menu_items = Menu.objects.filter(
        pk__in=quantities.keys(),
        available=True,
        home_cook__is_verified=True,
    )
    menu_by_id = {item.pk: item for item in menu_items}
    if len(menu_by_id) != len(quantities):
        return JsonResponse(
            {
                "error": (
                    "One or more meals are unavailable. "
                    "Refresh your cart and try again."
                )
            },
            status=400,
        )
    try:
        with transaction.atomic():
            profile.primary_mobile_number = digits
            profile.save(update_fields=["primary_mobile_number"])
            order = Order.objects.create(
                customer=profile,
                address=address,
                payment_mode="cod",
            )
            for menu_id, quantity in quantities.items():
                menu_item = menu_by_id[menu_id]
                OrderItem.objects.create(
                    order=order,
                    menu_item=menu_item,
                    name=menu_item.name,
                    price=menu_item.price,
                    quantity=quantity,
                )
            order.calculate_totals()
    except Exception:
        # Roll back the order and avoid exposing internal database errors.
        return JsonResponse(
            {
                "error": (
                    "We couldn't place your order. "
                    "Please try again."
                )
            },
            status=500,
        )
    return JsonResponse(
        {
            "success": True,
            "order_id": order.pk,
            "redirect_url": reverse("order_history"),
        },
        status=201,
    )




