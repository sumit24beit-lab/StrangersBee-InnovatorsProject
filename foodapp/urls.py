from django.urls import path
from .views import home_page_view, cart_page_view, menu_page_view, restaurant_page_view, delivery_page_view, contact_page_view, offers_page_view

urlpatterns = [ 
    path('home/',home_page_view,name='home'),
    path('cart/',cart_page_view,name='cart'),
    path('menu/',menu_page_view,name='menu'),
    path('restaurant/',restaurant_page_view,name='restaurant'),
    path('delivery/',delivery_page_view,name='delivery'),
    path('contact/',contact_page_view,name='contact'),
    path('offers/',offers_page_view,name='offers'),
]