from django.contrib import admin
from .models import HomeCook
# Register your models here.

@admin.register(HomeCook)
class HomeCookAdmin(admin.ModelAdmin):
    list_display = (
        "kitchen_name",
        "cook_name",
        "city",
        "specialty_cuisine",
        "is_verified",
    )
    list_filter = (
        "city",
        "specialty_cuisine",
        "is_verified",
    )
    search_fields = (
        "kitchen_name",
        "cook_name",
        "area",
        "city",
    )
