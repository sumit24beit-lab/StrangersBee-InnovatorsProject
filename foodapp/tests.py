from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import TestCase
from decimal import Decimal
from home_cooks.models import HomeCook
from accounts.models import AccountProfile
from .models import (
    CustomerProfile, 
    Address,
    Menu,
    Order,
    OrderItem,
    Offer,
)
import json

User=get_user_model()

# Create your tests here.
class OrderCalculationTests(TestCase):
    def setUp(self):
        # Create a customer for the test orders.
        self.customer = CustomerProfile.objects.create(
            user="test_customer",
            first_name="Aditi",
            last_name="Shah",
            email="aditi.test@example.com",
        )
        self.address = Address.objects.create(
            customer=self.customer,
            address_line="Test Address",
            city="Mumbai",
            area="Andheri",
            pincode="400001",
            address_type="home",
        )
        self.cook_user = User.objects.create_user(
            username="test_cook",
            password="test-password-123",
        )
        self.home_cook = HomeCook.objects.create(
            user=self.cook_user,
            cook_name="Test Cook",
            kitchen_name="Test Home Kitchen",
            area="Andheri",
            city="Mumbai",
            specialty_cuisine="north_indian",
        )
        self.meal = Menu.objects.create(
            home_cook=self.home_cook,
            name="Test Meal",
            price=Decimal("100.00"),
            category="lunch"
        )
    def create_order(self, quantity):
        order = Order.objects.create(
            customer=self.customer,
            address=self.address,
        )
        OrderItem.objects.create(
            order=order,
            menu_item=self.meal,
            name=self.meal.name,
            price=Decimal("100.00"),
            quantity=quantity,
        )
        # Verify that the item is linked to the order.
        self.assertEqual(
            order.items.count(),
            1,
            "Expected one OrderItem linked to this order"
        )
        # Calculate and save the order totals.
        order.calculate_totals()
        return order
    def test_standard_delivery_charge(self):
        order = self.create_order(quantity=2)
        self.assertEqual(order.subtotal, Decimal("200.00"))
        self.assertEqual(order.tax, Decimal("10.00"))
        self.assertEqual(order.delivery_charge, Decimal("40.00"),)
        self.assertEqual(order.total, Decimal("250.00"))
    def test_delivery_charge_at_exactly_500(self):
        order = self.create_order(quantity=5)
        self.assertEqual(order.subtotal, Decimal("500.00"))
        self.assertEqual(order.tax, Decimal("25.00"))
        self.assertEqual(order.delivery_charge, Decimal("40.00"),)
        self.assertEqual(order.total, Decimal("565.00"))
    def test_free_delivery_above_500(self):
        order = self.create_order(quantity=6)
        self.assertEqual(order.subtotal, Decimal("600.00"))
        self.assertEqual(order.tax, Decimal("30.00"))
        self.assertEqual(order.delivery_charge, Decimal("0.00"),)
        self.assertEqual(order.total, Decimal("630.00"))
    def test_offer_discounted_price(self):
        offer = Offer(
            menu_item=self.meal,
            original_price=Decimal("200.00"),
            discount_percent=20,
        )
        self.assertEqual(
            offer.discounted_price(),
            Decimal("160.00"),
        )

class CustomerCartAccessTests(TestCase):
    def setUp(self):
        self.customer = User.objects.create_user(
            username="cart_customer",
            password="TestPass@123",
        )
        AccountProfile.objects.create(
            user=self.customer,
            role=AccountProfile.CUSTOMER,
        )
        self.home_cook = User.objects.create_user(
            username="cart_homecook",
            password="TestPass@123",
        )
        AccountProfile.objects.create(
            user=self.home_cook,
            role=AccountProfile.HOME_COOK,
        )
    def test_logged_out_user_is_redirected_to_login(self):
        response = self.client.get(reverse("cart"))
        self.assertRedirects(
            response,
            reverse("accounts_login"),
        )
    def test_customer_can_access_cart(self):
        self.client.force_login(self.customer)
        response = self.client.get(reverse("cart"))
        self.assertEqual(response.status_code, 200)
    def test_home_cook_cannot_access_customer_cart(self):
        self.client.force_login(self.home_cook)
        response = self.client.get(reverse("cart"))
        self.assertRedirects(
            response,
            reverse("home"),
        )
    def test_customer_cannot_access_home_cook_management_pages(self):
        self.client.force_login(self.customer)
        protected_views = [
            "cook_dashboard",
            "my_profile",
            "my_meals",
            "add_meal",
            "cook_orders",
            "cook_earnings",
        ]
        for view_name in protected_views:
            with self.subTest(view=view_name):
                response = self.client.get(reverse(view_name))
                self.assertRedirects(
                    response,
                    reverse("home"),
                )

class AddressManagementTests(TestCase):
    def setUp(self):
        self.customer_user = User.objects.create_user(
            username="address_customer_one",
            email="customer.one@example.com",
            password="TestPass@123",
        )
        AccountProfile.objects.create(
            user=self.customer_user,
            role=AccountProfile.CUSTOMER,
        )
        self.customer_profile = CustomerProfile.objects.create(
            user=self.customer_user.username,
            first_name="Aditi",
            last_name="Shah",
            email=self.customer_user.email,
        )
        self.other_user = User.objects.create_user(
            username="address_customer_two",
            email="customer.two@example.com",
            password="TestPass@123",
        )
        AccountProfile.objects.create(
            user=self.other_user,
            role=AccountProfile.CUSTOMER,
        )
        self.other_profile = CustomerProfile.objects.create(
            user=self.other_user.username,
            first_name="Neha",
            last_name="Patil",
            email=self.other_user.email,
        )
        self.address = Address.objects.create(
            customer=self.customer_profile,
            address_line="Flat 204, Maple Residency",
            area="Powai",
            city="Mumbai",
            state="Maharashtra",
            pincode="400076",
            address_type="home",
        )
        self.other_address = Address.objects.create(
            customer=self.other_profile,
            address_line="Flat 12, Green Apartments",
            area="Andheri",
            city="Mumbai",
            state="Maharashtra",
            pincode="400053",
            address_type="office",
        )
    def valid_address_data(self):
        return {
            "address_line": "Flat 803, Silver Oak Apartments",
            "area": "Vikhroli East",
            "city": "Mumbai",
            "state": "Maharashtra",
            "pincode": "400083",
            "address_type": "office",
        }
    def test_customer_can_view_own_addresses(self):
        self.client.force_login(self.customer_user)
        response = self.client.get(reverse("customer_addresses"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Flat 204, Maple Residency")
        self.assertNotContains(response, "Flat 12, Green Apartments")
    def test_customer_can_add_address(self):
        self.client.force_login(self.customer_user)
        response = self.client.post(
            reverse("customer_address_add"),
            self.valid_address_data(),
        )
        self.assertRedirects(
            response,
            reverse("customer_addresses"),
        )
        address = Address.objects.get(
            address_line="Flat 803, Silver Oak Apartments"
        )
        self.assertEqual(address.customer, self.customer_profile)
    def test_customer_can_edit_own_address(self):
        self.client.force_login(self.customer_user)
        response = self.client.post(
            reverse(
                "customer_address_edit",
                args=[self.address.pk],
            ),
            self.valid_address_data(),
        )
        self.assertRedirects(
            response,
            reverse("customer_addresses"),
        )
        self.address.refresh_from_db()
        self.assertEqual(
            self.address.address_line,
            "Flat 803, Silver Oak Apartments",
        )
        self.assertEqual(self.address.area, "Vikhroli East")
        self.assertEqual(self.address.address_type, "office")
    def test_customer_can_delete_own_address(self):
        self.client.force_login(self.customer_user)
        response = self.client.post(
            reverse(
                "customer_address_delete",
                args=[self.address.pk],
            ),
        )
        self.assertRedirects(
            response,
            reverse("customer_addresses"),
        )
        self.assertFalse(
            Address.objects.filter(pk=self.address.pk).exists()
        )
    def test_customer_cannot_edit_another_customers_address(self):
        self.client.force_login(self.customer_user)
        original_address_line = self.other_address.address_line
        response = self.client.post(
            reverse(
                "customer_address_edit",
                args=[self.other_address.pk],
            ),
            self.valid_address_data(),
        )
        self.assertEqual(response.status_code, 404)
        self.other_address.refresh_from_db()
        self.assertEqual(
            self.other_address.address_line,
            original_address_line,
        )
    def test_customer_cannot_delete_another_customers_address(self):
        self.client.force_login(self.customer_user)
        response = self.client.post(
            reverse(
                "customer_address_delete",
                args=[self.other_address.pk],
            ),
        )
        self.assertEqual(response.status_code, 404)
        self.assertTrue(
            Address.objects.filter(pk=self.other_address.pk).exists()
        )

class OrderHistoryTests(TestCase):
    def setUp(self):
        self.customer_user = User.objects.create_user(
            username="history_customer_one",
            email="history.one@example.com",
            password="TestPass@123",
        )
        AccountProfile.objects.create(
            user=self.customer_user,
            role=AccountProfile.CUSTOMER,
        )
        self.customer = CustomerProfile.objects.create(
            user=self.customer_user.username,
            first_name="Aditi",
            last_name="Shah",
            email=self.customer_user.email,
        )
        self.address = Address.objects.create(
            customer=self.customer,
            address_line="Flat 204, Maple Residency",
            area="Powai",
            city="Mumbai",
            pincode="400076",
            address_type="home",
        )
        self.other_user = User.objects.create_user(
            username="history_customer_two",
            email="history.two@example.com",
            password="TestPass@123",    
        )
        AccountProfile.objects.create(
            user=self.other_user,
            role=AccountProfile.CUSTOMER,
        )
        self.other_customer = CustomerProfile.objects.create(
            user=self.other_user.username,
            first_name="Neha",
            last_name="Patil",
            email=self.other_user.email,
        )
        self.other_address = Address.objects.create(
            customer=self.other_customer,
            address_line="Flat 12, Green Apartments",
            area="Andheri",
            city="Mumbai",
            pincode="400053",
            address_type="office",
        )
    def create_order(self, customer, address, item_name):
        cook_user = User.objects.create_user(
            username=f"cook_for_{item_name.lower().replace(' ', '_')}",
            password="TestPass@123",
        )
        cook = HomeCook.objects.create(
            user=cook_user,
            cook_name="Test Cook",
            kitchen_name="Test Home Kitchen",
            area="Powai",
            city="Mumbai",
            specialty_cuisine="north_indian",
        )
        meal = Menu.objects.create(
            home_cook=cook,
            name=item_name,
            price=Decimal("120.00"),
            category="lunch",
        )
        order = Order.objects.create(
            customer=customer,
            address=address,
            subtotal=Decimal("120.00"),
            tax=Decimal("6.00"),
            delivery_charge=Decimal("40.00"),
            total=Decimal("166.00"),
        )
        OrderItem.objects.create(
            order=order,
            menu_item=meal,
            name=item_name,
            price=Decimal("120.00"),
            quantity=1,
        )
        return order
    def test_logged_out_user_is_redirected_to_login(self):
        response = self.client.get(reverse("order_history"))
        self.assertRedirects(
            response,
            reverse("accounts_login"),
        )
    def test_customer_sees_own_orders_only(self):
        self.create_order(
            self.customer,
            self.address,
            "Aditi Paneer Thali",
        )
        self.create_order(
            self.other_customer,
            self.other_address,
            "Neha Veg Pulao",
        )
        self.client.force_login(self.customer_user)
        response = self.client.get(reverse("order_history"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Aditi Paneer Thali")
        self.assertNotContains(response, "Neha Veg Pulao")
    def test_customer_with_no_orders_sees_empty_state(self):
        self.client.force_login(self.customer_user)
        response = self.client.get(reverse("order_history"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No orders yet")

class PlaceOrderTests(TestCase):
    def setUp(self):
        self.customer_user = User.objects.create_user(
            username="checkout_customer",
            email="checkout@example.com",
            password="TestPass@123",
        )
        AccountProfile.objects.create(
            user=self.customer_user,
            role=AccountProfile.CUSTOMER,
        )
        self.customer = CustomerProfile.objects.create(
            user=self.customer_user.username,
            first_name="Rohan",
            last_name="Deshmukh",
            email=self.customer_user.email,
        )
        self.address = Address.objects.create(
            customer=self.customer,
            address_line="Flat 502, Sunrise Residency",
            area="Ghatkopar West",
            city="Mumbai",
            state="Maharashtra",
            pincode="400086",
            address_type="home",
        )
        self.cook_user = User.objects.create_user(
            username="checkout_cook",
            password="TestPass@123",
        )
        self.cook = HomeCook.objects.create(
            user=self.cook_user,
            cook_name="Neha Kulkarni",
            kitchen_name="Neha's Fresh Kitchen",
            area="Powai",
            city="Mumbai",
            specialty_cuisine="north_indian",
            is_verified=True,
        )                
        self.meal = Menu.objects.create(
            home_cook=self.cook,
            name="Fresh Pav Bhaji (Homestyle Butter)",
            description="Fresh homemade pav bhaji.",
            price=Decimal("120.00"),
            category="lunch",
            ingredients="Vegetables, spices, bread and butter",
            available=True,
        )
        self.client.force_login(self.customer_user)
    def order_payload(self, **overrides):
        payload = {
            "phone": "9876543210",
            "address_id": self.address.pk,
            "payment_method": "cod",
            "items": [
                {
                    "id": self.meal.pk,
                    "qty": 1,
                    "name": "Fake Meal",
                    "price": 1,
                }
            ],
        }
        payload.update(overrides)
        return payload
    def post_order(self, payload):
        return self.client.post(
            reverse("place_order"),
            data=json.dumps(payload),
            content_type="application/json",
        )
    def test_successful_order_uses_database_price(self):
        response = self.post_order(self.order_payload())
        self.assertEqual(response.status_code, 201)
        result = response.json()
        self.assertTrue(result["success"])
        order = Order.objects.get(pk=result["order_id"])
        item = OrderItem.objects.get(order=order)
        self.assertEqual(order.customer, self.customer)
        self.assertEqual(order.address, self.address)
        self.assertEqual(order.status, "pending")
        self.assertEqual(item.menu_item, self.meal)
        self.assertEqual(item.name, self.meal.name)
        self.assertEqual(item.price, Decimal("120.00"))
        self.assertEqual(item.quantity, 1)
        self.assertEqual(order.subtotal, Decimal("120.00"))
        self.assertEqual(order.tax, Decimal("6.00"))
        self.assertEqual(order.delivery_charge, Decimal("40.00"))
        self.assertEqual(order.total, Decimal("166.00"))
    def test_unavailable_meal_is_rejected(self):
        self.meal.available = False
        self.meal.save(update_fields=["available"])
        response = self.post_order(self.order_payload())
        self.assertEqual(response.status_code, 400)
        self.assertEqual(Order.objects.count(), 0)
    def test_invalid_menu_id_is_rejected(self):
        payload = self.order_payload()
        payload["items"][0]["id"] = 999999
        response = self.post_order(payload)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(Order.objects.count(), 0)
    def test_address_belonging_to_another_customer_is_rejected(self):
        other_customer = CustomerProfile.objects.create(
            user="another_checkout_customer",
            first_name="Aditi",
            last_name="Shah",
            email="another@example.com",
        )
        other_address = Address.objects.create(
            customer=other_customer,
            address_line="Another address",
            area="Andheri",
            city="Mumbai",
            state="Maharashtra",
            pincode="400053",
            address_type="home",
        )
        payload = self.order_payload(address_id=other_address.pk)
        response = self.post_order(payload)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(Order.objects.count(), 0)
    def test_online_payment_is_rejected(self):
        payload = self.order_payload(payment_method="online")
        response = self.post_order(payload)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(Order.objects.count(), 0)
