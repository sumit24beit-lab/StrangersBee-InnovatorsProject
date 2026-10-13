from django.db import models
from django.conf import settings

CUISINE_CHOICES = [
    ("north_indian", "North Indian"),
    ("south_indian", "South Indian"),
    ("maharashtrian", "Maharashtrian"),
    ("gujarati", "Gujarati"),
    ("other", "Other"),
]
# Create your models here.
class HomeCook(models.Model):
    user=models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="home_cook_profile"
    )
    cook_name=models.CharField(max_length=200)
    kitchen_name=models.CharField(max_length=200)
    area=models.CharField(max_length=200)
    city=models.CharField(max_length=200)
    specialty_cuisine=models.CharField(max_length=30, choices=CUISINE_CHOICES)
    about=models.TextField(max_length=500,blank=True)
    is_verified=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"{self.kitchen_name} - {self.cook_name}"
