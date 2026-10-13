from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import HomeCook
from decimal import Decimal
from django.urls import reverse
from foodapp.models import Menu

# Create your tests here.
User = get_user_model()
class HomeCookModelTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="asha_test",
            email="asha@example.com",
            password="test-password-123",
        )
        self.home_cook = HomeCook.objects.create(
            user=self.user,
            cook_name="Asha",
            kitchen_name="Asha's Kitchen",
            area="Andheri West",
            city="Mumbai",
            specialty_cuisine="north_indian",
            about="Homemade North Indian meals.",
        )
    def test_home_cook_is_linked_to_user(self):
        self.assertEqual(self.home_cook.user, self.user)
        self.assertEqual(
            self.user.home_cook_profile,
            self.home_cook,
        )
    def test_new_home_cook_is_unverified(self):
        self.assertFalse(self.home_cook.is_verified)
    def test_home_cook_string_representation(self):
        self.assertEqual(
            str(self.home_cook),
            "Asha's Kitchen - Asha"
        )

class HomeCookViewTests(TestCase):
    def setUp(self):
        self.verified_user = User.objects.create_user(
            username="verified_cook",
            email="verified@example.com",
            password="test-password-123",
        )
        self.verified_cook=HomeCook.objects.create(
            user=self.verified_user,
            cook_name="Asha",
            kitchen_name="Asha's Kitchen",
            area="Andheri West",
            city="Mumbai",
            specialty_cuisine="north_indian",
            about="Homemade North Indian meals.",
            is_verified=True,
        )
        self.unverified_user=User.objects.create_user(
            username="unverified_cook",
            email="unverified@example.com",
            password="test-password-123",
        )
        self.unverified_cook=HomeCook.objects.create(
            user=self.unverified_user,
            cook_name="Riya",
            kitchen_name="Riya's Kitchen",
            area="Powai",
            city="Mumbai",
            specialty_cuisine="south_indian",
            about="Homemade South Indian meals.",
            is_verified=False,
        )
    def test_listing_shows_verified_cooks_only(self):
        response = self.client.get(reverse("home_cooks"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Asha's Kitchen")
        self.assertNotContains(response, "Riya's Kitchen")
    def test_verified_cook_profile_displays_details(self):
        url = reverse(
            "cook_profile_detail",
            args=[self.verified_cook.pk],
        )
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Asha&#x27;s Kitchen")
        self.assertContains(response, "Asha")
        self.assertContains(response, "Andheri West")
        self.assertContains(response, "Mumbai")
        self.assertContains(response, "North Indian")
        self.assertContains(response, "Homemade North Indian meals.")
    def test_unverified_cook_profile_returns_404(self):
        url = reverse(
            "cook_profile_detail",
            args=[self.unverified_cook.pk],
        )
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

class MealDetailViewTests(TestCase):
    def setUp(self):
        self.verified_user = User.objects.create_user(
            username="meal_cook",
            password="test-password-123",
        )
        self.verified_cook = HomeCook.objects.create(
            user=self.verified_user,
            cook_name="Asha",
            kitchen_name="Asha's Kitchen",
            area="Andheri West",
            city="Mumbai",
            specialty_cuisine="north_indian",
            about="Homemade North Indian meals.",
            is_verified=True,
        )
        self.meal = Menu.objects.create(
            home_cook=self.verified_cook,
            name="Homestyle Paneer Thali",
            description="Paneer curry, dal, vegetables, roti and rice.",
            price=Decimal("180.00"),
            category="lunch",
            ingredients="Paneer, dal, vegetables, rice and wheat roti.",
            available=True,
        )
        self.unverified_user = User.objects.create_user(
            username="unverified_meal_cook",
            password="test-password-123",
        )
        self.unverified_cook = HomeCook.objects.create(
            user=self.unverified_user,
            cook_name="Riya",
            kitchen_name="Riya's Kitchen",
            area="Powai",
            city="Mumbai",
            specialty_cuisine="south_indian",
            about="Homemade South Indian meals.",
            is_verified=False,
        )
        self.unverified_meal = Menu.objects.create(
            home_cook=self.unverified_cook,
            name="Unverified Kitchen Meal",
            description="Test meal",
            price=Decimal("100.00"),
            category="lunch",
            available=True,
        )
    def test_available_meal_displays_details(self):
        url = reverse(
            "meal_detail_by_id",
            args=[self.meal.pk],
        )
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Homestyle Paneer Thali")
        self.assertContains(response, "180.00")
        self.assertContains(response, "Asha&#x27;s Kitchen")
        self.assertContains(response, "Andheri West")
        self.assertContains(response, "Paneer curry, dal")
    def test_unavailable_meal_returns_404(self):
            self.meal.available=False
            self.meal.save(update_fields=["available"])
            url = reverse(
                "meal_detail_by_id",
                args=[self.meal.pk],
            )
            response = self.client.get(url)
            self.assertEqual(response.status_code, 404)
    def test_meal_from_unverified_cook_returns_404(self):
            url = reverse(
                "meal_detail_by_id",
                args=[self.unverified_meal.pk],
            )
            response = self.client.get(url)
            self.assertEqual(response.status_code, 404)
            
            
    
