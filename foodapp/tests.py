from django.contrib.auth import get_user_model
from django.test import TestCase
from decimal import Decimal
from home_cooks.models import HomeCook
from .models import (
    CustomerProfile, 
    Address,
    Menu,
    Order,
    OrderItem,
    Offer,
)

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