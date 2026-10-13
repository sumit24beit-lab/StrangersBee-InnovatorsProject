from django import forms
from .models import HomeCook
from foodapp.models import Menu

class HomeCookForm(forms.ModelForm):
    class Meta:
        model = HomeCook
        fields = (
            "cook_name",
            "kitchen_name",
            "area",
            "city",
            "specialty_cuisine",
            "about",
        )
        labels = {
            "cook_name": "Cook Name",
            "kitchen_name": "Kitchen Name",
            "area": "Area",
            "city": "City",
            "specialty_cuisine": "Specialty Cuisine",
            "about": "About Your Kitchen",
        }
        widgets = {
            "cook_name": forms.TextInput(attrs={
                "class": "form-control ks-form-control",
                "id": "cookName",
                "autocomplete": "name",
            }),
            "kitchen_name": forms.TextInput(attrs={
                "class": "form-control ks-form-control",
                "id": "kitchenName",
            }),
            "area": forms.TextInput(attrs={
                "class": "form-control ks-form-control",
                "id": "location",
            }),
            "city": forms.TextInput(attrs={
                "class": "form-control ks-form-control",
                "id": "city",
            }),
            "specialty_cuisine": forms.Select(attrs={
                "class": "form-select ks-form-control",
                "id": "specialty",
            }),
            "about": forms.Textarea(attrs={
                "class": "form-control ks-form-control my-profile-textarea",
                "id": "about",
                "rows": 5,
                "placeholder": (
                    "Describe your cooking style, favourite recipes, "
                    "and the meals you prepare..."
                ),
            }),
        }

class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = (
            "name",
            "description",
            "price",
            "category",
            "image",
            "ingredients",
            "nutrients",
            "spice_level",
            "meal_time",
            "food_type",
            "nutrient_function",
            "available"
        )
        labels = {
            "name": "Meal Name",
            "description": "Description",
            "price": "Price (₹)",
            "category": "Meal Category",
            "image": "Meal Image",
            "ingredients": "Ingredients",
            "nutrients": "Nutritional Information",
            "spice_level": "Spice Level",
            "meal_time": "Suitable Meal Time",
            "food_type": "Food Type",
            "nutrient_function": "Nutritional Category",
            "available": "Available for Orders",
        }
        widgets = {
            "name": forms.TextInput(attrs={
                "class": "form-control ks-form-control",
            }),
            "description": forms.Textarea(attrs={
                "class": "form-control ks-form-control",
                "rows": 3,
            }),
            "price": forms.NumberInput(attrs={
                "class": "form-control ks-form-control",
                "min": "0.01",
                "step": "0.01",
            }),
            "category": forms.Select(attrs={
                "class": "form-select ks-form-control",
            }),
            "image": forms.ClearableFileInput(attrs={
                "class": "form-control ks-form-control",
            }),
            "ingredients": forms.Textarea(attrs={
                "class": "form-control ks-form-control",
                "rows": 3,
            }),
            "nutrients": forms.TextInput(attrs={
                "class": "form-control ks-form-control",
            }),
            "spice_level": forms.Select(attrs={
                "class": "form-select ks-form-control",
            }),
            "meal_time": forms.Select(attrs={
                "class": "form-select ks-form-control",
            }),
            "food_type": forms.Select(attrs={
                "class": "form-select ks-form-control",
            }),
            "nutrient_function": forms.Select(attrs={
                "class": "form-select ks-form-control",
            }),
            "available": forms.CheckboxInput(attrs={
                "class": "form-check-input",
            }),
        }
