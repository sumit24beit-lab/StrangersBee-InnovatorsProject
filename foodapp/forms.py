from django import forms
from django.contrib.auth.models import User
from .models import (
    CustomerProfile,
    Address,
    Restaurant,
    Menu,
    Offer,
    Order,
    OrderItem,
    Contact,
    FoodReview,
    CustomerFeedback,
)

class SignupForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields=['username','email','password']
    def clean_username(self):
        username=self.cleaned_data.get('username')
        if not username.isalnum() or len(username)<3:
            raise forms.ValidationError("Username must be at least 3 characters and alphanumeric")            
        return username
    def clean_email(self):
        email=self.cleaned_data.get('email', '')
        if not email.lower().endswith('@gmail.com'):
            raise forms.ValidationError("Email must be a valid Gmail address")
        return email
    def clean_password(self):
        password=self.cleaned_data.get('password')
        if len(password) < 8:
            raise forms.ValidationError("Password must be at least 8 characters")
        return password
    
class CustomerProfileForm(forms.ModelForm):
    class Meta:
        model = CustomerProfile
        fields = [
            "first_name",
            "middle_name",
            "last_name",
            "primary_mobile_number",
            "alternate_mobile_number",
        ]
        widgets = {
            "first_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter first name",
                }
            ),
            "middle_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter middle name",
                }
            ),
            "last_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter last name",
                }
            ),
            "primary_mobile_number": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter primary mobile number",
                    "inputmode": "numeric",
                    "maxlength": "10",
                }
            ),
            "alternate_mobile_number": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter alternate mobile number",
                    "inputmode": "numeric",
                    "maxlength": "10",
                }
            ),
        }

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = [
            "address_line",
            "area",
            "city",
            "state",
            "pincode",
            "address_type",
        ]
        widgets = {
            "address_line": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "House number, street, building",
            }),
            "area": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter area or locality",
            }),
            "city": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter city",
            }),
            "state": forms.TextInput(attrs={
                "class": "form-control",
            }),
            "pincode": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter PIN code",
                "maxlength": "10",
            }),
            "address_type": forms.Select(attrs={
                "class": "form-select",
            }),
        }

class FoodReviewForm(forms.ModelForm):
    class Meta:
        model = FoodReview
        fields = [
            "menu_item",
            "rating",
            "title",
            "review_text",
            "photo",
        ]
        widgets = {
            "menu_item": forms.Select(
                attrs={"class": "form-select"}
            ),
            "rating": forms.Select(
                attrs={"class": "form-select"}
            ),
            "title": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Give your review a title",
                }
            ),
            "review_text": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Describe your food experience",
                    "rows": 4,
                }
            ),
            "photo": forms.ClearableFileInput(
                attrs={
                    "class": "form-control",
                    "accept": "image/*",
                }
            ),
        }
    def __init__(self, *args, customer_profile=None, **kwargs):
        super().__init__(*args, **kwargs)
        if customer_profile is None:
            self.fields["menu_item"].queryset = Menu.objects.none()
        else:
            self.fields["menu_item"].queryset = (
                Menu.objects.filter(
                    orderitem__order__customer=customer_profile,
                    orderitem__order__status="delivery",
                )
                .distinct()
                .order_by("name")
            )
    def clean_photo(self):
        photo = self.cleaned_data.get("photo")
        if photo and photo.size > 5 * 1024 * 1024:
            raise forms.ValidationError(
                "The photo must be 5 MB or smaller."
            )
        return photo

class CustomerFeedbackForm(forms.ModelForm):
    class Meta:
        model = CustomerFeedback
        fields = [
            "feedback_type",
            "subject",
            "message",
            "order",
        ]
        widgets = {
            "feedback_type": forms.Select(
                attrs={"class": "form-select"}
            ),
            "subject": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter a subject",
                }
            ),
            "message": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Describe your feedback or complaint",
                    "rows": 5,
                }
            ),
            "order": forms.Select(
                attrs={"class": "form-select"}
            ),
        }
    def __init__(self, *args, customer_profile=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["order"].required = False
        if customer_profile is None:
            self.fields["order"].queryset = Order.objects.none()
        else:
            self.fields["order"].queryset =  (
                Order.objects.filter(customer=customer_profile)
                .order_by("-created_at")
            )
