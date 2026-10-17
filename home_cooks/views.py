from django.shortcuts import render, get_object_or_404, redirect
from .models import HomeCook
from django.db.models import Prefetch
from foodapp.models import Menu, Order, OrderItem
from django.contrib import messages
from .decorators import home_cook_required
from .forms import HomeCookForm, MenuForm
from django.views.decorators.http import require_POST
from decimal import Decimal
from django.utils import timezone

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

@home_cook_required
def dashboard_view(request):
    cook = HomeCook.objects.filter(user=request.user).first()
    if cook is None:
        messages.warning(
            request,
            "Please complete your home cook profile first.",
        )
        return redirect("my_profile")
    meals = Menu.objects.filter(home_cook=cook)
    total_meals = meals.count()
    available_meals = meals.filter(available=True).count()
    orders = (
        Order.objects
        .filter(items__menu_item__home_cook=cook)
        .distinct()
        .prefetch_related(
            Prefetch(
                "items",
                queryset=OrderItem.objects.select_related("menu_item"),
            )
        )
        .order_by("-created_at")
    )
    order_entries = []
    for order in orders:
        all_items = list(order.items.all())
        cook_items = [
            item
            for item in all_items
            if (
                item.menu_item_id is not None
                and item.menu_item.home_cook_id == cook.pk
            )
        ]
        if not cook_items:
            continue
        cook_subtotal = sum(
            (
                item.price * item.quantity
                for item in cook_items
            ),
            Decimal("0.00"),
        )
        order_entries.append({
            "order": order,
            "cook_items": cook_items,
            "cook_subtotal": cook_subtotal,
        })
    new_orders_count = sum(
        entry["order"].status == "pending"
        for entry in order_entries
    )
    completed_orders_count = sum(
        entry["order"].status == "delivery"
        for entry in order_entries
    )
    accepting_orders = cook.is_verified and available_meals > 0
    return render(
        request,
        'home_cooks/dashboard.html',
        {
            "cook": cook,
            "total_meals": total_meals,
            "available_meals": available_meals,
            "new_orders_count": new_orders_count,
            "completed_orders_count": completed_orders_count,
            "recent_orders": order_entries[:5],
            "accepting_orders": accepting_orders,
        },
    )

@home_cook_required
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

@home_cook_required
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

@home_cook_required
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

@home_cook_required
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

@home_cook_required
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

@home_cook_required
def cook_orders_view(request):
    cook = HomeCook.objects.filter(user=request.user).first()
    if cook is None:
        messages.warning(
            request,
            "Please complete your home cook profile first.",
        )
        return redirect("my_profile")
    orders = (
        Order.objects
        .filter(items__menu_item__home_cook=cook)
        .distinct()
        .select_related("customer", "address")
        .prefetch_related(
            Prefetch(
                "items",
                queryset=OrderItem.objects.select_related("menu_item"),
            )
        )
        .order_by("-created_at")
    )
    order_entries = []
    for order in orders:
        all_items = list(order.items.all())
        cook_items = [
            item
            for item in all_items
            if (
                item.menu_item_id is not None
                and item.menu_item.home_cook_id == cook.pk
            )
        ]
        # Order.status is shared by every item in that order.
        # Do not let one cook update an order containing another
        # kitchen's meals or items whose cook cannot be identified.
        can_manage_status = (
            bool(all_items)
            and len(cook_items) == len(all_items)
        )
        order_entries.append({
            "order": order,
            "cook_items": cook_items,
            "can_manage_status": can_manage_status,
        })
    new_orders_count = sum(
        entry["order"].status == "pending"
        for entry in order_entries
    )
    preparing_orders_count = sum(
        entry["order"].status == "preparing"
        for entry in order_entries
    )
    delivered_orders_count = sum(
        entry["order"].status == "delivery"
        for entry in order_entries
    )
    return render(
        request,
        'home_cooks/cook_orders.html',
        {
            "order_entries": order_entries,
            "new_orders_count": new_orders_count,
            "preparing_orders_count": preparing_orders_count,
            "delivered_orders_count": delivered_orders_count,
        },
    )

@home_cook_required
@require_POST
def update_cook_order_status_view(request, order_id):
    cook = HomeCook.objects.filter(user=request.user).first()
    if cook is None:
        messages.warning(
            request,
            "Please complete your home cook profile first.",
        )
        return redirect("my_profile")
    order = get_object_or_404(
        Order.objects.filter(
            items__menu_item__home_cook=cook,
        ).distinct(),
        pk=order_id,
    )
    items = list(order.items.select_related("menu_item"))
    # The status belongs to the whole order. Protect other kitchens.
    if (
        not items
        or any(
            item.menu_item_id is None
            or item.menu_item.home_cook_id != cook.pk
            for item in items
        )
    ):
        messages.error(
            request,
            "This order cannot be updated because it contains "
            "items outside your kitchen.",
        )
        return redirect("cook_orders")
    allowed_transitions = {
        "pending": {"preparing", "cancelled"},
        "preparing": {"on_the_way"},
        "on_the_way": {"delivery"},
        "delivery": set(),
        "cancelled": set(),
    }
    new_status = request.POST.get("status", "")
    if new_status not in allowed_transitions.get(order.status, set()):
        messages.error(
            request,
            "That status change is not allowed.",
        )
        return redirect("cook_orders")
    order.status = new_status
    order.save(update_fields=["status"])
    status_messages = {
        "preparing": "Order accepted. Preparation can begin.",
        "cancelled": "Order rejected.",
        "on_the_way": "Order marked as on the way.",
        "delivery": "Order marked as delivered",
    }
    messages.success(
        request,
        status_messages[new_status],
    )
    return redirect("cook_orders")

@home_cook_required
def cook_earnings_view(request):
    cook = HomeCook.objects.filter(user=request.user).first()
    if cook is None:
        messages.warning(
            request,
            "Please complete your home cook profile first.",
        )
        return redirect("my_profile")
    orders = (
        Order.objects
        .filter(items__menu_item__home_cook=cook)
        .distinct()
        .prefetch_related(
            Prefetch(
                "items",
                queryset=OrderItem.objects.select_related("menu_item"),
            )
        )
        .order_by("-created_at")
    )
    order_entries = []
    for order in orders:
        cook_items = [
            item
            for item in order.items.all()
            if (
                item.menu_item_id is not None
                and item.menu_item.home_cook_id == cook.pk
            )
        ]
        if not cook_items:
            continue
        # Count only this cook's meal value, not delivery charges or tax.
        cook_subtotal = sum(
            (
                item.price * item.quantity
                for item in cook_items
            ),
            Decimal("0.00"),
        )
        order_entries.append({
            "order": order,
            "cook_items": cook_items,
            "cook_subtotal": cook_subtotal,
        })
    delivered_entries = [
        entry
        for entry in order_entries
        if entry["order"].status == "delivery"
    ]
    today = timezone.localdate()
    monthly_delivered_entries = [
        entry
        for entry in delivered_entries
        if (
            timezone.localtime(
                entry["order"].created_at
            ).year == today.year
            and timezone.localtime(
                entry["order"].created_at
            ).month == today.month
        )
    ]
    total_sales = sum(
        (entry["cook_subtotal"] for entry in delivered_entries),
        Decimal("0.00"),
    )
    monthly_sales = sum(
        (
            entry["cook_subtotal"]
            for entry in monthly_delivered_entries
        ),
        Decimal("0.00"),
    )
    sales_awaiting_delivery = sum(
        (
            entry["cook_subtotal"]
            for entry in order_entries
            if entry["order"].status in {
                "pending",
                "preparing",
                "on_the_way",
            }
        ),
        Decimal("0.00"),
    )
    return render(
        request,
        'home_cooks/cook_earnings.html',
        {
            "total_sales": total_sales,
            "monthly_sales": monthly_sales,
            "completed_orders_count": len(delivered_entries),
            "sales_awaiting_delivery": sales_awaiting_delivery,
            "recent_transactions": delivered_entries[:5],
            "payout_tracking_configured": False,
        },
    )
