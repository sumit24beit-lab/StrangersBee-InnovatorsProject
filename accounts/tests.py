from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from foodapp.models import CustomerProfile
from home_cooks.models import HomeCook
from .models import AccountProfile

User = get_user_model()
TEST_PASSWORD = "KitchenStation!Test927"

# Create your tests here.
class AccountSignupTests(TestCase):
    def signup_data(self, **overrides):
        data = {
            "full_name": "Alice Example",
            "username": "alice2026",
            "email": "alice@example.com",
            "password1": TEST_PASSWORD,
            "password2": TEST_PASSWORD,
            "role": AccountProfile.CUSTOMER,
            "accept_terms": "on",
        }
        data.update(overrides)
        return data
    def test_signup_page_loads(self):
        response = self.client.get(reverse("accounts_signup"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Create your account")
    def test_customer_signup_creates_user_and_profile(self):
        response = self.client.post(
            reverse("accounts_signup"),
            self.signup_data(),
        )
        self.assertRedirects(response, reverse("accounts_login"))
        user = User.objects.get(username="alice2026")
        self.assertTrue(user.check_password(TEST_PASSWORD))
        self.assertNotEqual(user.password, TEST_PASSWORD)
        account_profile = AccountProfile.objects.get(user=user)
        self.assertEqual(account_profile.role, AccountProfile.CUSTOMER)
        customer = CustomerProfile.objects.get(email="alice@example.com")
        self.assertEqual(customer.user, user.username)
        self.assertEqual(customer.first_name, "Alice")
        self.assertEqual(customer.last_name, "Example")
    def test_home_cook_signup_creates_unverified_cook_profile(self):
        response = self.client.post(
            reverse("accounts_signup"),
            self.signup_data(
                username="cook2026",
                email="cook@example.com",
                role=AccountProfile.HOME_COOK,
                cook_name="Alice",
                kitchen_name="Alice's Kitchen",
                area="Andheri",
                city="Mumbai",
                specialty_cuisine="maharashtrian",
                about="Homemade Maharashtrian meals",
            ),
        )
        self.assertRedirects(response, reverse("accounts_login"))
        user = User.objects.get(username="cook2026")
        self.assertEqual(
            AccountProfile.objects.get(user=user).role,
            AccountProfile.HOME_COOK,
        )
        cook = HomeCook.objects.get(user=user)
        self.assertEqual(cook.kitchen_name, "Alice's Kitchen")
        self.assertFalse(cook.is_verified)
    def test_password_mismatch_prevents_signup(self):
        response = self.client.post(
            reverse("accounts_signup"),
            self.signup_data(password2="DifferentPassword!927"),
        )
        self.assertEqual(response.status_code, 200)
        self.assertFalse(User.objects.filter(username="alice2026").exists())
        self.assertContains(response, "passwords do not match")
    def test_home_cook_signup_requires_kitchen_details(self):
        response = self.client.post(
            reverse("accounts_signup"),
            self.signup_data(
                role=AccountProfile.HOME_COOK,
                kitchen_name="",
            ),
        )
        self.assertEqual(response.status_code, 200)
        self.assertFalse(User.objects.filter(username="alice2026").exists())

class AccountLoginLogoutTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="existinguser",
            email="existing@example.com",
            password=TEST_PASSWORD,
        )
        AccountProfile.objects.create(
            user=self.user,
            role=AccountProfile.CUSTOMER,
        )
    def test_login_page_loads(self):
        response = self.client.get(reverse("accounts_login"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Welcome back")
    def test_login_with_email_and_password(self):
        response = self.client.post(
            reverse("accounts_login"),
            {
                "email": "existing@example.com",
                "password": TEST_PASSWORD,
            },
        )
        self.assertRedirects(response, reverse("home"))
        self.assertIn("_auth_user_id", self.client.session)
        self.assertEqual(
            str(self.client.session["_auth_user_id"]),
            str(self.user.pk),
        )
    def test_invalid_password_does_not_log_in(self):
        response = self.client.post(
            reverse("accounts_login"),
            {
                "email": "existing@example.com",
                "password": "WrongPassword!927",
            },
        )
        self.assertEqual(response.status_code, 200)
        self.assertNotIn("_auth_user_id", self.client.session)
        self.assertContains(response, "incorrect")
    def test_logout_clears_session(self):
        self.client.force_login(self.user)
        response = self.client.post(reverse("accounts_logout"))
        self.assertRedirects(response, reverse("accounts_login"))
        self.assertNotIn("_auth_user_id", self.client.session)
    def test_get_request_does_not_log_out_user(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("accounts_logout"))
        self.assertRedirects(response, reverse("home"))
        self.assertIn("_auth_user_id", self.client.session)

        
