from django.contrib import admin
from .models import Customer,Address,Restaurant,Menu,Offer,Order,OrderItem,Contact

# Register your models here.
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('user','email','password','phone','date_joined')
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
    list_display = ('name','restaurant','price','available','spice_level','meal_time','food_type','nutrient_function')
    list_filter = ('restaurant','available','spice_level','meal_time','food_type')
    search_fields = ('name','ingredients')

@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
    list_display = ('menu_item','discount_price','offer_valid_until')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer','address', 'total')  

@admin.register(OrderItem)
class ItemAdmin(admin.ModelAdmin):
    list_display=('order','menu_item','name','price','quantity')

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):   
    list_display=('name','email','subject','created_at')  
