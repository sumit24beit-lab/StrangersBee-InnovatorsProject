from django.urls import path
from .views import home_cooks_view, cook_profile_view, kitchen_details_view, cook_meals_view, meal_details_view, dashboard_view, my_profile_view, my_meals_view, cook_orders_view, cook_earnings_view

urlpatterns = [
    path('',home_cooks_view, name='home_cooks'),
    path('cook_profile/', cook_profile_view, name='cook_profile'),
    path('kitchen_details/', kitchen_details_view, name='kitchen_details'),
    path('cook-meals/', cook_meals_view, name='cook_meals'),
    path('meal-details/', meal_details_view, name='meal_details'),
    path('dashboard/', dashboard_view, name='cook_dashboard'),
    path('my-profile/', my_profile_view, name='my_profile'),
    path('my-meals/', my_meals_view, name='my_meals'),
    path('orders/', cook_orders_view, name='cook_orders'),
    path('earnings/', cook_earnings_view, name='cook_earnings'),
]