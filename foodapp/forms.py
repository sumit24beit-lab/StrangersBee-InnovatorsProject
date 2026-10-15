from django import forms
from django.contrib.auth.models import User
from.models import CustomerProfile, Address, Restaurant, Menu, Offer, Order, OrderItem, Contact

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
