from django.urls import path
from .views import signup_view, login_view, home_page_view, cart_view, menu_view, restaurant_view, delivery_view, contact_view, offers_view

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
]
