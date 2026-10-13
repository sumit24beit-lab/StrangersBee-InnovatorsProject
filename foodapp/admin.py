from django.contrib import admin
from .models import CustomerProfile,Address,Restaurant,Menu,Offer,Order,OrderItem,Contact

# Register your models here.
@admin.register(CustomerProfile)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('user', 'email', 'primary_mobile_number', 'date_joined')

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0    

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
     list_display = ('customer','address_line','city', 'state') 

@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name', 'address','isluxury')  

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'home_cook',
        'price',
        'available',
        'spice_level',
        'meal_time',
        'food_type',
        'nutrient_function',
    )
    list_filter = (
        'home_cook',
        'available',
        'spice_level',
        'meal_time',
        'food_type',
    )
    search_fields = ('name','ingredients')

@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
    list_display = ('menu_item', 'original_price', 'discount_percent', 'offer_valid_until', )

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer','address', 'total')  

@admin.register(OrderItem)
class ItemAdmin(admin.ModelAdmin):
    list_display=('order','menu_item','name','price','quantity')

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):   
    list_display=('customer','email','subject','created_at')  
