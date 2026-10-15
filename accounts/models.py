from django.conf import settings
from django.db import models

# Create your models here.
class AccountProfile(models.Model):
    CUSTOMER = "customer"
    HOME_COOK = "home_cook"
    ROLE_CHOICES = [
        (CUSTOMER, "Customer"),
        (HOME_COOK, "Home Cook"),
    ]
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="account_profile",
    )
    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default=CUSTOMER,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"{self.user.username} - {self.get_role_display()}"
