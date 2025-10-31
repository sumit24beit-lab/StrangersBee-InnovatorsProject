from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

# Create your models here.

# Helper choices
SPICE_CHOICES = [
    ('spicy', 'Spicy'),
    ('normal', 'Normal'),
    ('not', 'Not Spicy'),
]

MEAL_CHOICES = [
    ('breakfast','Breakfast'),
    ('lunch','Lunch'),
    ('dinner','Dinner'),
    ('snack','Snack'),
    ('dessert','Dessert'),
]

TYPE_CHOICES = [
    ('liquid','Liquid'),
    ('light','Light'),
    ('heavy','Heavy'),
    ('solid','Solid'),
]


NUTRI_CHOICES = [
    ('fruits','Fruits & Vegetables'),
    ('starchy','Starchy Carbohydrates'),
    ('protein','Protein Foods'),
    ('dairy','Dairy & Alternatives'),
    ('fats','Fats & Oils'),
]

ORDER_CHOICE=[
    ('preparing','Preparing'),
    ('pending','Pending'),
    ('on_the_way','On the way'),
    ('delivery','Delivery'),
    ('cancelled','Cancelled'),
]

class Customer(models.Model):
    user=models.CharField(max_length=200)
    email=models.EmailField()
    password=models.CharField(max_length=200,blank=True)
    phone=models.CharField(max_length=20)
    date_joined=models.DateTimeField(auto_now_add=True)
    is_active=models.BooleanField(default=True)
    def __str__(self):
        return self.name

class Address(models.Model):
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE,related_name="customer_addresses")
    address_line=models.CharField(max_length=400)
    city=models.CharField(max_length=120)
    area=models.CharField(max_length=120)
    state=models.CharField(max_length=160,default='Maharashtra')
    pincode=models.CharField(max_length=10,default=True)
    address_type=models.CharField(max_length=200,choices=[('home','Home'),('office','Office'),('other','Other')])
    created_at_date=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.address_line}-{self.city}"
    
class Restaurant(models.Model):
    name=models.CharField(max_length=200)
    address=models.TextField()
    city=models.CharField(max_length=200,blank=True)
    area=models.CharField(max_length=200,blank=True)
    rating=models.DecimalField(max_digits=3,decimal_places=1,default=0.0)
    avg_prize_for_two=models.PositiveIntegerField(default=200)
    isverified=models.BooleanField(default=False)
    isluxury=models.CharField(max_length=200,choices=[('high','High'),('medium','Medium'),('low','Low')])
    image=models.ImageField(upload_to="static/foodapp/image/restaurants/",blank=True,null=True)
    description=models.TextField(blank=True)
    created_at_date=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

class Menu(models.Model):
    restaurant=models.ForeignKey(Restaurant,on_delete=models.CASCADE,related_name="menu_items")
    name=models.CharField(max_length=200)
    description=models.TextField(blank=True)
    price=models.DecimalField(max_digits=8,decimal_places=2)
    category=models.CharField(max_length=250,choices=[('breakfast','Breakfast'),('lunch','Lunch'),('dinner','Dinner'),('snack','Snack'),('tea','Tea')])
    nutrients = models.CharField(max_length=250, blank=True)  # short summary
    ingredients = models.TextField(blank=True)
    image = models.ImageField(upload_to='menu_items/', blank=True, null=True)
    available = models.BooleanField(default=True)
    spice_level = models.CharField(max_length=10, choices=SPICE_CHOICES, default='normal')
    meal_time = models.CharField(max_length=20, choices=MEAL_CHOICES, default='lunch')
    food_type = models.CharField(max_length=10, choices=TYPE_CHOICES, default='heavy')
    nutrient_function = models.CharField(max_length=20, choices=NUTRI_CHOICES, default='starchy')
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.name}-{self.restaurant.name}"
    
class Offer(models.Model):
    menu_item=models.ForeignKey(Menu,on_delete=models.CASCADE,related_name="offers")
    original_price=models.DecimalField(max_digits=8,decimal_places=2)
    discount_price=models.PositiveIntegerField(default=0)
    offer_valid_until=models.DateTimeField(blank=True,null=True)    
    def discounted_price(self):
        return round(float(self.menu_item.price) * (1 - (self.discount_percent/100.0)), 2)
    def __str__(self):
        return f"{self.menu_item.name} ({self.discount_price}% off)"

class Order(models.Model):
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE,related_name="orders")
    address=models.ForeignKey(Address,on_delete=models.CASCADE,related_name="orders")
    created_at=models.DateTimeField(auto_now_add=True)
    status=models.CharField(max_length=20,choices=ORDER_CHOICE,default='pending')
    delivery_charge=models.DecimalField(max_digits=6,decimal_places=2,default=40.00)
    subtotal=models.DecimalField(max_digits=10,decimal_places=2,default=0.0)
    tax=models.DecimalField(max_digits=7,decimal_places=2,default=0.0)
    total=models.DecimalField(max_digits=10,decimal_places=2,default=0.0)
    payment_mode=models.CharField(max_length=20,blank=True,default=True)
    def calculate_totals(self):
        items = self.items.all()
        subtotal = sum([it.price * it.quantity for it in items])
        tax = round(subtotal * 0.05, 2)
        delivery_fee = self.delivery_fee if subtotal < 500 else 0.00
        total = round(subtotal + tax + delivery_fee, 2)
        self.subtotal = subtotal
        self.tax = tax
        self.total = total
        self.save()
        return self.total
    def __str__(self):
        return f"Order: {self.id}-{self.customer.name if self.customer else 'Guest'}"    

class OrderItem(models.Model):
    order=models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    menu_item=models.ForeignKey(Menu, on_delete=models.SET_NULL, null=True)
    name=models.CharField(max_length=240)
    price=models.DecimalField(max_digits=8, decimal_places=2)
    quantity=models.PositiveIntegerField(default=1)
    notes=models.CharField(max_length=300, blank=True)
    def line_total(self):
        return round(self.price * self.quantity, 2)
    def __str__(self):
        return f"{self.quantity} x {self.name}"    

class Contact(models.Model):
    name=models.ForeignKey(Customer,on_delete=models.CASCADE,related_name='contact')
    email=models.CharField()
    subject=models.CharField(max_length=200)
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

    