from functools import wraps
from django.contrib import messages
from django.shortcuts import redirect
from accounts.models import AccountProfile

def customer_required(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect("accounts_login")
        profile = AccountProfile.objects.filter(
            user=request.user
        ).only("role").first()
        if profile is None or profile.role != AccountProfile.CUSTOMER:
            messages.error(
                request,
                "This page is available to Customer accounts only.",
            )
            return redirect("home")
        return view_func(request, *args, **kwargs)
    return wrapper

        