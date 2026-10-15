import re
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError

from .models import AccountProfile
from home_cooks.models import HomeCook, CUISINE_CHOICES

User = get_user_model()

class AccountSignupForm(forms.Form):
    full_name = forms.CharField(
        max_length=200,
        label="Full name",
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "autocomplete": "name",
            "placeholder": "Enter your full name",
        }),
    )
    username = forms.CharField(
        min_length=3,
        max_length=150,
        label="Username",
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "autocomplete": "username",
            "placeholder": "Choose a username",
        }),
    )
    email = forms.EmailField(
        label="Email address",
        widget=forms.EmailInput(attrs={
            "class": "form-control",
            "autocomplete": "email",
            "placeholder": "you@example.com",
        }),
    )
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={
            "class": "form-control",
            "autocomplete": "new-password",
            "placeholder": "Create a password",
        }),
    )
    password2 = forms.CharField(
        label="Confirm password",
        widget=forms.PasswordInput(attrs={
            "class": "form-control",
            "autocomplete": "new-password",
            "placeholder": "Enter your password again",
        }),
    )
    role = forms.ChoiceField(
        label="Account type",
        choices=AccountProfile.ROLE_CHOICES,
        widget=forms.Select(attrs={
            "class": "form-select",
        }),
    )
    accept_terms = forms.BooleanField(
        required=True,
        label="I accept the Terms & Conditions",
    )

    # These fields are required only for Home Cook registration.
    cook_name = forms.CharField(
        max_length=200,
        required=False,
        label="Cook name",
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Name shown to customers",
        }),
    )
    kitchen_name = forms.CharField(
        max_length=200,
        required=False,
        label="Kitchen name",
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": " Your kitchen or cooking business name",
        }),
    )
    area = forms.CharField(
        max_length=200,
        required=False,
        label="Area",
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Your locality",
        }),
    )
    city = forms.CharField(
        max_length=200,
        required=False,
        label="City",
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Your city",
        }),
    )
    specialty_cuisine = forms.ChoiceField(
        required=False,
        label="Specialty cuisine",
        choices=[("", "Select a cuisine")] + list(CUISINE_CHOICES),
        widget=forms.Select(attrs={
            "class": "form-select",
        }),
    )
    about = forms.CharField(
        required=False,
        max_length=500,
        label="About your kitchen",
        widget=forms.Textarea(attrs={
            "class": "form-control",
            "rows": 4,
            "placeholder": "Describe your cooking style and specialties",
        }),
    )

    def clean_username(self):
        username = self.cleaned_data["username"].strip()
        if not re.fullmatch(r"[A-Za-z0-9_]+", username):
            raise forms.ValidationError("Username may contain letters, numbers, and underscores only.")
        if User.objects.filter(username__iexact=username).exists():
            raise forms.ValidationError("This username is already taken.")
        return username
    def clean_email(self):
        email = self.cleaned_data["email"].strip()
        if User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError("An account with this email address already exists.")
        return email
    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")
        role = cleaned_data.get("role")
        if password1 and password2 and password1 != password2:
            self.add_error("password2","The passwords do not match.")
        if password1:
            full_name = cleaned_data.get("full_name", "").strip()
            name_parts = full_name.split()
            user = User(
                username=cleaned_data.get("username", ""),
                email=cleaned_data.get("email", ""),
                first_name=name_parts[0] if name_parts else "",
            )
            try:
                validate_password(password1, user=user)
            except ValidationError as error:
                self.add_error("password1", error)
        if role == AccountProfile.HOME_COOK:
            required_fields = {
                "cook_name": "Enter the cook name.",
                "kitchen_name": "Enter the kitchen name.",
                "area": "Enter your area.",
                "city": "Enter your city.",
                "specialty_cuisine": "Select a specialty cuisine.",
            }
            for field_name, message in required_fields.items():
                if not cleaned_data.get(field_name):
                    self.add_error(field_name, message)
        return cleaned_data

class AccountLoginForm(forms.Form):
    email = forms.EmailField(
        label="Email address",
        widget=forms.EmailInput(attrs={
            "class": "form-control",
            "autocomplete": "email",
            "placeholder": "you@example.com",
        }),
    )
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={
            "class": "form-control",
            "autocomplete": "current-password",
            "placeholder": "Enter your password",
        }),
    )


    