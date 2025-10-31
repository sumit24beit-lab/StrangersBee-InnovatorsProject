from django.urls import path
from .views import signup_page_view,login_page_view,home_page_view, cart_page_view, menu_page_view, restaurant_page_view, restaurant_list_view, delivery_page_view, contact_page_view, offers_page_view, restaurant_list_view

urlpatterns = [
    path('signup/',signup_page_view,name='signup'),
    path('login/',login_page_view,name='login'),
    path('home/',home_page_view,name='home'),
    path('cart/',cart_page_view,name='cart'),
    path('menu/',menu_page_view,name='menu'),
    path('restaurant/',restaurant_page_view,name='restaurant'),
    path('delivery/',delivery_page_view,name='delivery'),
    path('contact/',contact_page_view,name='contact'),
    path('offers/',offers_page_view,name='offers'),
    path('restaurants/', restaurant_list_view, name='restaurant_list')
]