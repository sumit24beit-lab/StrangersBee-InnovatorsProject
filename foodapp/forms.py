from django import forms
from django.contrib.auth.models import User
from.models import CustomerProfile, Address, Restaurant, Menu, Offer, Order, OrderItem, Contact

class SignupForm(forms.ModelForm):
    password=forms.CharField(Widget=forms.PasswordInput)
    class Meta:
        model = User
        fields=['username','email','password']
        def clean_username(self):
            username=self.cleaned_data.get('username')
            if not username.isalnum() or len(username)<3:
                raise forms.ValidationError("Username must be at least 3 characters and alphanumeric")
            return username
        def clean_email(self):
            email=self.cleaned_data.get('email')
            if not email.endswith('@gmail.com'):
                raise forms.ValidationError("Email must be a valid gmail address")
            return email
        def clean_password(self):
            password=self.cleaned_data.get('password')
            if len(password)>8:
                raise forms.ValidationError("Password must be at least 8 characters")
            return password
class CustomerProfileForm(forms.ModelForm):
