from django.urls import path
from .views import (
    signup_view, 
    login_view, 
    home_page_view, 
    cart_view, 
    menu_view, 
    restaurant_view, 
    delivery_view, 
    contact_view, 
    offers_view, 
    customer_profile_view,
    customer_addresses_view,
    customer_address_add_view,
    customer_address_edit_view,
    customer_address_delete_view,
    order_history_view,
    place_order_view,
)

urlpatterns = [
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('home/', home_page_view, name='home'),
    path('cart/', cart_view, name='cart'),
    path('menu/', menu_view, name='menu'),
    path('restaurant/', restaurant_view, name='restaurant'),
    path('delivery/', delivery_view, name='delivery'),
    path('contact/', contact_view, name='contact'),
    path('offers/', offers_view, name='offers'),
    path('customer/profile/', customer_profile_view,  name='customer_profile'),
    path('customer/addresses/', customer_addresses_view, name='customer_addresses'),
    path('customer/addresses/add/', customer_address_add_view, name='customer_address_add'),
    path('customer/addresses/<int:address_id>/edit/', customer_address_edit_view, name='customer_address_edit'),
    path('customer/addresses/<int:address_id>/delete/', customer_address_delete_view, name='customer_address_delete'),
    path('customer/orders/', order_history_view, name='order_history'),
    path('customer/orders/place/', place_order_view, name='place_order')
]
