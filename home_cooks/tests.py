from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import HomeCook
from decimal import Decimal
from django.urls import reverse
from foodapp.models import (
    Address,
    CustomerProfile,
    Menu,
    Order,
    OrderItem,
)
from accounts.models import AccountProfile

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

class HomeCookProfileEditTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="profile_editor",
            email="profile@example.com",
            password="test-password-123",
        )
        AccountProfile.objects.create(
            user=self.user,
            role=AccountProfile.HOME_COOK,
        )
    def valid_profile_data(self):
        return {
            "cook_name": "Asha",
            "kitchen_name": "Asha's Kitchen",
            "area": "Andheri West",
            "city": "Mumbai",
            "specialty_cuisine": "north_indian",
            "about": "Homemade North Indian meals.",
        }
    def test_profile_page_requires_login(self):
        response = self.client.get(
            reverse("my_profile")
        )
        self.assertEqual(response.status_code, 302)
        self.assertIn(reverse("login"), response.url)
    def test_logged_in_cook_can_view_profile_form(self):
        self.client.force_login(self.user)
        response = self.client.get(
            reverse("my_profile")
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "My Profile")
        self.assertContains(response, 'name="cook_name"')
        self.assertContains(response, 'name="kitchen_name"')
    def test_logged_in_cook_can_create_profile(self):
        self.client.force_login(self.user)
        response = self.client.post(
            reverse("my_profile"),
            self.valid_profile_data(),
        )
        self.assertEqual(response.status_code, 302)
        profile = HomeCook.objects.get(user=self.user)
        self.assertEqual(profile.cook_name, "Asha")
        self.assertEqual(
            profile.kitchen_name,
            "Asha's Kitchen",
        )
        self.assertFalse(profile.is_verified)
    def test_logged_in_cook_can_update_own_profile(self):
        profile = HomeCook.objects.create(
            user=self.user,
            cook_name="Asha",
            kitchen_name="Old Kitchen",
            area="Andheri",
            city="Mumbai",
            specialty_cuisine="north_indian",
            is_verified=True,
        )
        self.client.force_login(self.user)
        data = self.valid_profile_data()
        data["kitchen_name"] = "Updated Kitchen"
        response = self.client.post(
            reverse("my_profile"),
            data,
        )
        self.assertEqual(response.status_code, 302)
        profile.refresh_from_db()
        self.assertEqual(profile.kitchen_name, "Updated Kitchen",)
        self.assertTrue(profile.is_verified)
    def test_invalid_profile_is_not_saved(self):
        self.client.force_login(self.user)
        data = self.valid_profile_data()
        data["cook_name"] = ""
        response = self.client.post(
            reverse("my_profile"),
            data,
        )
        self.assertEqual(response.status_code, 200)
        self.assertFalse(
            HomeCook.objects.filter(user=self.user).exists()
        )

class MealManagementTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="meal_owner",
            password="test-password-123",
        )
        AccountProfile.objects.create(
                    user=self.user,
                    role=AccountProfile.HOME_COOK,
        )
        self.cook = HomeCook.objects.create(
            user=self.user,
            cook_name="Asha",
            kitchen_name="Asha's Kitchen",
            area="Andheri West",
            city="Mumbai",
            specialty_cuisine="north_indian",
        )
        self.other_user = User.objects.create_user(
            username="other_cook",
            password="test-password-123",
        )
        self.other_cook = HomeCook.objects.create(
            user=self.other_user,
            cook_name="Riya",
            kitchen_name="Riya's Kitchen",
            area="Powai",
            city="Mumbai",
            specialty_cuisine="south_indian",
        )
    def valid_meal_data(self):
        return {
            "name": "Homestyle Paneer Thali",
            "description": "Paneer, dal, rice and roti.",
            "price": "180.00",
            "category": "lunch",
            "ingredients": "Paneer, dal, rice, wheat roti",
            "nutrients": "Protein and carbohydrates",
            "spice_level": "normal",
            "meal_time": "lunch",
            "food_type": "heavy",
            "nutrient_function": "protein",
            "available": "on",
        }
    def test_add_meal_requires_login(self):
        response=self.client.get(reverse("add_meal"))
        self.assertEqual(response.status_code, 302)
        self.assertIn(reverse("login"), response.url)
    def test_logged_in_cook_can_open_add_meal_form(self):
        self.client.force_login(self.user)
        response=self.client.get(reverse("add_meal"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Add New Meal")
        self.assertContains(response, 'name="name"')
    def test_meal_is_created_for_logged_in_cook(self):
        self.client.force_login(self.user)
        data=self.valid_meal_data()
        data["home_cook"]=str(self.other_cook.pk)
        response=self.client.post(reverse("add_meal"), data,)
        self.assertRedirects(response, reverse("my_meals"))
        meal=Menu.objects.get(name="Homestyle Paneer Thali")
        self.assertEqual(meal.home_cook, self.cook)
        self.assertEqual(meal.price, Decimal("180.00"))
        self.assertTrue(meal.available)
    def test_invalid_meal_is_not_saved(self):
        self.client.force_login(self.user)
        data=self.valid_meal_data()
        data["name"]=""
        response=self.client.post(reverse("add_meal"), data,)
        self.assertEqual(response.status_code, 200)
        self.assertFalse(
            Menu.objects.filter(
                home_cook=self.cook
            ).exists()
        )
    def test_account_without_cook_profile_is_redirected(self):
        user_without_profile = User.objects.create_user(
            username="customer_without_cook_profile",
            password="test-password-123",
        )
        AccountProfile.objects.update_or_create(
            user=user_without_profile,
            defaults={"role": AccountProfile.HOME_COOK},
        )
        self.client.force_login(user_without_profile)
        response=self.client.get(reverse("add_meal"))
        self.assertRedirects(
            response,
            reverse("my_profile"),
        )

class MealOwnershipTests(TestCase):
    def setUp(self):
        self.user=User.objects.create_user(
            username="cook_one",
            password="test-password-123",
        )
        AccountProfile.objects.create(
                    user=self.user,
                    role=AccountProfile.HOME_COOK,
        )
        self.cook=HomeCook.objects.create(
            user=self.user,
            cook_name="Asha",
            kitchen_name="Asha's Kitchen",
            area="Andheri West",
            city="Mumbai",
            specialty_cuisine="north_indian",
        )
        self.other_user=User.objects.create_user(
            username="cook_two",
            password="test-password-123",
        )
        self.other_cook=HomeCook.objects.create(
            user=self.other_user,
            cook_name="Riya",
            kitchen_name="Riya's Kitchen",
            area="Powai",
            city="Mumbai",
            specialty_cuisine="south_indian",
        )
        self.own_meal=Menu.objects.create(
            home_cook=self.cook,
            name="Asha's Thali",
            description="Homemade meal",
            price=Decimal("180.00"),
            category="lunch",
            available=True,
        )
        self.other_meal=Menu.objects.create(
            home_cook=self.other_cook,
            name="Riya's Pulao",
            description="Vegetable pulao",
            price=Decimal("120.00"),
            category="lunch",
            available=True,
        )
    def test_cook_can_edit_own_meal(self):
        self.client.force_login(self.user)
        response = self.client.post(
            reverse("edit_meal", args=[self.own_meal.pk]),
            {
                "name": "Updated Asha Thali",
                "description": "Updated description",
                "price": "200.00",
                "category": "lunch",
                "ingredients": "Rice, vegetables",
                "nutrients": "Carbohydrates",
                "spice_level": "normal",
                "meal_time": "lunch",
                "food_type": "heavy",
                "nutrient_function": "starchy",
                "available": "on",
            },
        )
        self.assertRedirects(response, reverse("my_meals"))
        self.own_meal.refresh_from_db()
        self.assertEqual(self.own_meal.name, "Updated Asha Thali")
        self.assertEqual(self.own_meal.home_cook, self.cook)
    def test_cook_cannot_edit_another_cooks_meal(self):
        self.client.force_login(self.user)
        response=self.client.get(reverse("edit_meal", args=[self.other_meal.pk]))
        self.assertEqual(response.status_code, 404)
        self.other_meal.refresh_from_db()
        self.assertEqual(self.other_meal.name, "Riya's Pulao")
    def test_cook_can_toggle_own_meal_availability(self):
        self.client.force_login(self.user)
        response=self.client.post(reverse("toggle_meal_availability", args=[self.own_meal.pk],))
        self.assertRedirects(response, reverse("my_meals"))
        self.own_meal.refresh_from_db()
        self.assertFalse(self.own_meal.available)
    def test_cook_cannot_toggle_another_cooks_meal(self):
        self.client.force_login(self.user)
        response = self.client.post(reverse("toggle_meal_availability", args=[self.other_meal.pk],))
        self.assertEqual(response.status_code, 404)
        self.other_meal.refresh_from_db()
        self.assertTrue(self.other_meal.available)

class CookOrderManagementTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="asha_order_test",
            password="test-password-123",
        )
        AccountProfile.objects.create(
            user=self.user,
            role=AccountProfile.HOME_COOK,
        )
        self.cook = HomeCook.objects.create(
            user=self.user,
            cook_name="Asha",
            kitchen_name="Asha's Kitchen",
            area="Andheri West",
            city="Mumbai",
            specialty_cuisine="north_indian",
            is_verified=True,
        )
        self.other_user = User.objects.create_user(
            username="riya_order_test",
            password="test-password-123",
        )
        AccountProfile.objects.create(
            user=self.other_user,
            role=AccountProfile.HOME_COOK,
        )
        self.other_cook = HomeCook.objects.create(
            user=self.other_user,
            cook_name="Riya",
            kitchen_name="Riya's Kitchen",
            area="Powai",
            city="Mumbai",
            specialty_cuisine="south_indian",
            is_verified=True,
        )
        self.customer = CustomerProfile.objects.create(
            user="test_customer",
            first_name="Rahul",
            last_name="Sharma",
            email="rahul@example.com",
        )
        self.address = Address.objects.create(
            customer=self.customer,
            address_line="101 Sample Road",
            area="Andheri West",
            city="Mumbai",
            state="Maharashtra",
            pincode="400053",
            address_type="home",
        )
        self.own_meal = Menu.objects.create(
            home_cook=self.cook,
            name="Asha's Paneer Thali",
            description="Homemade paneer thali",
            price=Decimal("180.00"),
            category="lunch",
            available=True,
        )
        self.other_meal = Menu.objects.create(
            home_cook=self.other_cook,
            name="Riya's Vegetable Pulao",
            description="Homemade vegetable pulao",
            price=Decimal("120.00"),
            category="lunch",
            available=True,
        )
        self.client.force_login(self.user)
    def create_order(self, status="pending", mixed_kitchens=False):
        order = Order.objects.create(
            customer=self.customer,
            address=self.address,
            status=status,
            payment_mode="cod",
        )
        OrderItem.objects.create(
            order=order,
            menu_item=self.own_meal,
            name=self.own_meal.name,
            price=self.own_meal.price,
            quantity=1,
        )
        if mixed_kitchens:
            OrderItem.objects.create(
                order=order,
                menu_item=self.other_meal,
                name=self.other_meal.name,
                price=self.other_meal.price,
                quantity=1,
            )
        return order
    def test_orders_page_shows_only_orders_containing_own_meals(self):
        own_order = self.create_order()
        other_order = Order.objects.create(
            customer=self.customer,
            address=self.address,
            status="pending",
            payment_mode="cod",
        )
        OrderItem.objects.create(
            order=other_order,
            menu_item=self.other_meal,
            name=self.other_meal.name,
            price=self.other_meal.price,
            quantity=1,
        )
        response = self.client.get(reverse("cook_orders"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, f"#KS{own_order.pk}")
        self.assertNotContains(response, f"#KS{other_order.pk}")
    def test_cook_can_accept_pending_order(self):
        order = self.create_order()
        response = self.client.post(
            reverse("update_cook_order_status", args=[order.pk]),
            {"status": "preparing"},
        )
        self.assertRedirects(response, reverse("cook_orders"))
        order.refresh_from_db()
        self.assertEqual(order.status, "preparing")
    def test_cook_can_reject_pending_order(self):
        order = self.create_order()
        response = self.client.post(
            reverse("update_cook_order_status", args=[order.pk]),
            {"status": "cancelled"},
        )
        self.assertRedirects(response, reverse("cook_orders"))
        order.refresh_from_db()
        self.assertEqual(order.status, "cancelled")
    def test_cook_can_progress_order_to_delivered(self):
        order = self.create_order(status="preparing")
        response = self.client.post(
            reverse("update_cook_order_status", args=[order.pk]),
            {"status": "on_the_way"},
        )
        self.assertRedirects(response, reverse("cook_orders"))
        order.refresh_from_db()
        self.assertEqual(order.status, "on_the_way")
        response = self.client.post(
            reverse("update_cook_order_status", args=[order.pk]),
            {"status": "delivery"},
        )
        self.assertRedirects(response, reverse("cook_orders"))
        order.refresh_from_db()
        self.assertEqual(order.status, "delivery")
    def test_invalid_status_transition_is_rejected(self):
        order = self.create_order(status="pending")
        response = self.client.post(
            reverse("update_cook_order_status", args=[order.pk]),
            {"status": "delivery"},
        )
        self.assertRedirects(response, reverse("cook_orders"))
        order.refresh_from_db()
        self.assertEqual(order.status, "pending")
    def test_cook_cannot_update_another_kitchens_order(self):
        order = Order.objects.create(
            customer=self.customer,
            address=self.address,
            status="pending",
            payment_mode="cod",
        )
        OrderItem.objects.create(
            order=order,
            menu_item=self.other_meal,
            name=self.other_meal.name,
            price=self.other_meal.price,
            quantity=1,
        )
        response = self.client.post(
            reverse("update_cook_order_status", args=[order.pk]),
            {"status": "preparing"},
        )
        self.assertEqual(response.status_code, 404)
        order.refresh_from_db()
        self.assertEqual(order.status, "pending")
    def test_mixed_kitchen_order_cannot_be_updated(self):
        order = self.create_order(mixed_kitchens=True)
        response = self.client.post(
            reverse("update_cook_order_status", args=[order.pk]),
            {"status": "preparing"},
        )
        self.assertRedirects(response, reverse("cook_orders"))
        order.refresh_from_db()
        self.assertEqual(order.status, "pending")

class CookEarningsViewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="earnings_cook",
            password="test-password-123",
        )
        AccountProfile.objects.create(
            user=self.user,
            role=AccountProfile.HOME_COOK,
        )
        self.cook = HomeCook.objects.create(
            user=self.user,
            cook_name="Asha",
            kitchen_name="Asha's Kitchen",
            area="Andheri West",
            city="Mumbai",
            specialty_cuisine="north_indian",
            is_verified=True,
        )
        self.other_user = User.objects.create_user(
            username="earnings_other_cook",
            password="test-password-123",
        )
        AccountProfile.objects.create(
            user=self.other_user,
            role=AccountProfile.HOME_COOK,
        )
        self.other_cook = HomeCook.objects.create(
            user=self.other_user,
            cook_name="Riya",
            kitchen_name="Riya's Kitchen",
            area="Powai",
            city="Mumbai",
            specialty_cuisine="south_indian",
            is_verified=True,
        )
        self.customer = CustomerProfile.objects.create(
            user="earnings_customer",
            first_name="Rahul",
            last_name="Sharma",
            email="earnings_customer@example.com",
        )
        self.address = Address.objects.create(
            customer=self.customer,
            address_line="101 Sample Road",
            area="Andheri West",
            city="Mumbai",
            state="Maharashtra",
            pincode="400053",
            address_type="home",
        )
        self.meal = Menu.objects.create(
            home_cook=self.cook,
            name="Asha's Paneer Thali",
            description="Paneer, rice and roti",
            price=Decimal("180.00"),
            category="lunch",
            available=True,
        )
        self.other_meal = Menu.objects.create(
            home_cook=self.other_cook,
            name="Riya's Vegetable Pulao",
            description="Homemade vegetable pulao",
            price=Decimal("120.00"),
            category="lunch",
            available=True,
        )
        self.client.force_login(self.user)
    def create_order(self, status, meal=None, quantity=1):
        meal = meal or self.meal
        order = Order.objects.create(
            customer=self.customer,
            address=self.address,
            status=status,
            payment_mode="cod",
        )
        OrderItem.objects.create(
            order=order,
            menu_item=meal,
            name=meal.name,
            price=meal.price,
            quantity=quantity,
        )
        return order
    def test_earnings_page_requires_home_cook_login(self):
        self.client.logout()
        response = self.client.get(reverse("cook_earnings"))
        self.assertEqual(response.status_code, 302)
    def test_only_delivered_orders_count_towards_sales(self):
        self.create_order(status="delivery")
        self.create_order(status="cancelled", quantity=2)
        self.create_order(status="pending")
        response=self.client.get(reverse("cook_earnings"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.context["total_sales"],
            Decimal("180.00"),
        )
        self.assertEqual(
            response.context["monthly_sales"],
            Decimal("180.00"),
        )
        self.assertEqual(
            response.context["completed_orders_count"],
            1,
        )
    def test_undelivered_orders_are_counted_separately(self):
        self.create_order(status="pending")
        self.create_order(status="preparing")
        self.create_order(status="on_the_way")
        self.create_order(status="cancelled")
        response=self.client.get(reverse("cook_earnings"))
        self.assertEqual(
            response.context["sales_awaiting_delivery"],
            Decimal("540.00"),
        )
        self.assertEqual(
            response.context["total_sales"],
            Decimal("0.00"),
        )
        self.assertEqual(
            response.context["completed_orders_count"],
            0,
        )
    def test_earnings_include_only_this_cooks_meals(self):
        order = Order.objects.create(
            customer=self.customer,
            address=self.address,
            status="delivery",
            payment_mode="cod",
        )
        OrderItem.objects.create(
            order=order,
            menu_item=self.meal,
            name=self.meal.name,
            price=self.meal.price,
            quantity=1,
        )
        OrderItem.objects.create(
            order=order,
            menu_item=self.other_meal,
            name=self.other_meal.name,
            price=self.other_meal.price,
            quantity=1,
        )
        response = self.client.get(reverse("cook_earnings"))
        self.assertEqual(
            response.context["total_sales"],
            Decimal("180.00"),
        )
        self.assertEqual(
            response.context["completed_orders_count"],
            1,
        )
    def test_recent_transactions_show_only_delivered_orders(self):
        delivered_order = self.create_order(status="delivery")
        self.create_order(status="pending")
        self.create_order(status="delivery",meal=self.other_meal)
        response=self.client.get(reverse("cook_earnings"))
        transactions=response.context["recent_transactions"]
        self.assertEqual(len(transactions), 1)
        self.assertEqual(
            transactions[0]["order"].pk,
            delivered_order.pk,
        )

class CookDashboardTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="dashboard_cook",
            password="test-password-123",
        )
        AccountProfile.objects.create(
            user=self.user,
            role=AccountProfile.HOME_COOK,
        )
        self.cook = HomeCook.objects.create(
            user=self.user,
            cook_name="Asha",
            kitchen_name="Asha's Kitchen",
            area="Andheri West",
            city="Mumbai",
            specialty_cuisine="north_indian",
            about="Homemade North Indian meals.",
            is_verified=True,
        )
        self.other_user = User.objects.create_user(
            username="dashboard_other_cook",
            password="test-password-123",
        )
        AccountProfile.objects.create(
            user=self.other_user,
            role=AccountProfile.HOME_COOK,
        )
        self.other_cook = HomeCook.objects.create(
            user=self.other_user,
            cook_name="Riya",
            kitchen_name="Riya's Kitchen",
            area="Powai",
            city="Mumbai",
            specialty_cuisine="south_indian",
            about="Homemade South Indian meals.",
            is_verified=True,
        )
        self.customer = CustomerProfile.objects.create(
            user="dashboard_customer",
            first_name="Rahul",
            last_name="Sharma",
            email="dashboard_customer@example.com",
        )
        self.address = Address.objects.create(
            customer=self.customer,
            address_line="101 Sample Road",
            area="Andheri West",
            city="Mumbai",
            state="Maharashtra",
            pincode="400053",
            address_type="home",
        )
        self.meal = Menu.objects.create(
            home_cook=self.cook,
            name="Asha's Paneer Thali",
            description="Paneer, rice and roti",
            price=Decimal("180.00"),
            category="lunch",
            available=True,
        )
        self.unavailable_meal = Menu.objects.create(
            home_cook=self.cook,
            name="Asha's Special Pulao",
            description="Homemade vegetable pulao",
            price=Decimal("120.00"),
            category="lunch",
            available=False,
        )
        self.other_meal = Menu.objects.create(
            home_cook=self.other_cook,
            name="Riya's Vegetable Pulao",
            description="Homemade vegetable pulao",
            price=Decimal("120.00"),
            category="lunch",
            available=True,
        )
        self.client.force_login(self.user)
    def create_order(self, status, meal=None, quantity=1):
        meal = meal or self.meal
        order = Order.objects.create(
            customer=self.customer,
            address=self.address,
            status=status,
            payment_mode="cod",
        )
        OrderItem.objects.create(
            order=order,
            menu_item=meal,
            name=meal.name,
            price=meal.price,
            quantity=quantity,
        )
        return order
    def test_dashboard_requires_login(self):
        self.client.logout()
        response=self.client.get(reverse("cook_dashboard"))
        self.assertEqual(response.status_code, 302)
    def test_dashboard_redirects_cook_without_profile(self):
        user_without_profile = User.objects.create_user(
            username="dashboard_no_profile",
            password="test-password-123",
        )
        AccountProfile.objects.create(
            user=user_without_profile,
            role=AccountProfile.HOME_COOK,
        )
        self.client.force_login(user_without_profile)
        response=self.client.get(reverse("cook_dashboard"))
        self.assertRedirects(response, reverse("my_profile"))
    def test_dashboard_displays_database_metrics(self):
        self.create_order(status="pending")
        delivered_order = self.create_order(
            status="delivery",
            quantity=2,
        )
        self.create_order(status="cancelled")
        other_order=self.create_order(
            status="pending",
            meal=self.other_meal,
        )
        response=self.client.get(reverse("cook_dashboard"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["cook"], self.cook)
        self.assertEqual(response.context["total_meals"], 2)
        self.assertEqual(response.context["available_meals"], 1)
        self.assertEqual(response.context["new_orders_count"], 1)
        self.assertEqual(
            response.context["completed_orders_count"],
            1,
        )
        self.assertTrue(response.context["accepting_orders"])
        recent_orders = response.context["recent_orders"]
        recent_order_ids = {
            entry["order"].pk for entry in recent_orders
        }
        self.assertIn(delivered_order.pk, recent_order_ids)
        self.assertNotIn(other_order.pk, recent_order_ids)
        delivered_entry = next(
            entry
            for entry in recent_orders
            if entry["order"].pk == delivered_order.pk
        )
        self.assertEqual(
            delivered_entry["cook_subtotal"],
            Decimal("360.00"),
        )
    def test_dashboard_counts_only_own_meal_value_in_mixed_order(self):
        order = Order.objects.create(
            customer=self.customer,
            address=self.address,
            status="delivery",
            payment_mode="cod",
        )
        OrderItem.objects.create(
            order=order,
            menu_item=self.meal,
            name=self.meal.name,
            price=self.meal.price,
            quantity=1,
        )
        OrderItem.objects.create(
            order=order,
            menu_item=self.other_meal,
            name=self.other_meal.name,
            price=self.other_meal.price,
            quantity=1,
        )
        response = self.client.get(reverse("cook_dashboard"))
        self.assertEqual(response.status_code, 200)
        entry = next(
            entry
            for entry in response.context["recent_orders"]
            if entry["order"].pk == order.pk
        )
        self.assertEqual(
            entry["cook_subtotal"],
            Decimal("180.00"),
        )
