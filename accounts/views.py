from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.db import transaction

from foodapp.models import CustomerProfile
from home_cooks.models import HomeCook

from .forms import AccountLoginForm, AccountSignupForm
from .models import AccountProfile

User = get_user_model()

# Create your views here.
def get_user_role(user):
    profile = AccountProfile.objects.filter(user=user).first()
    return profile.role if profile else None
def signup_view(request):
    if request.user.is_authenticated:
        return redirect("home")
    form = AccountSignupForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        full_name = form.cleaned_data["full_name"].strip()
        name_parts = full_name.split()
        first_name = name_parts[0]
        last_name = " ".join(name_parts[1:])
        with transaction.atomic():
            user = User.objects.create_user(
                username=form.cleaned_data["username"],
                email=form.cleaned_data["email"],
                password=form.cleaned_data["password1"],
                first_name=first_name,
                last_name=last_name,
            )
            role = form.cleaned_data["role"]
            AccountProfile.objects.create(user=user, role=role)
            if role == AccountProfile.CUSTOMER:
                CustomerProfile.objects.create(
                    user=user.username,
                    first_name=first_name,
                    last_name=last_name,
                    email=user.email,
                )
            elif role == AccountProfile.HOME_COOK:
                HomeCook.objects.create(
                    user=user,
                    cook_name=form.cleaned_data["cook_name"].strip(),
                    kitchen_name=form.cleaned_data["kitchen_name"].strip(),
                    area=form.cleaned_data["area"].strip(),
                    city=form.cleaned_data["city"].strip(),
                    specialty_cuisine=form.cleaned_data["specialty_cuisine"],
                    about=form.cleaned_data["about"].strip(),
                )
        messages.success(request,"Your account has been created. Please log in.",)
        return redirect("accounts_login")
    return render(request, 'accounts/signup.html', {"form": form},)

def login_view(request):
    if request.user.is_authenticated:
        role = get_user_role(request.user)
        if role == AccountProfile.HOME_COOK:
            return redirect("cook_dashboard")
        return redirect("home")
    form = AccountLoginForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        email = form.cleaned_data["email"].strip()
        password = form.cleaned_data["password"]
        account = User.objects.filter(email__iexact=email).first()
        user = None
        if account is not None:
            user = authenticate(request, username=account.username, password=password,)
        if user is not None:
            login(request, user)
            messages.success(request, "You are now logged in.")
            role = get_user_role(user)
            if role == AccountProfile.HOME_COOK:
                return redirect("cook_dashboard")
            return redirect("home")
        form.add_error(None, "Email address or password is incorrect.",)
    return render(request, 'accounts/login.html', {"form": form})

def logout_view(request):
    if request.method == "POST":
        logout(request)
        messages.success(request, "You have been logged out.")
        return redirect("accounts_login")
    return redirect("home")