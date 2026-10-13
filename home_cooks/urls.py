from django.urls import path
from .views import home_cooks_view, cook_profile_view, kitchen_details_view, cook_meals_view, meal_details_view, dashboard_view, my_profile_view, my_meals_view, cook_orders_view, cook_earnings_view, add_meal_view, edit_meal_view, toggle_meal_availability_view

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
    path('cook_profile/<int:cook_id>/', cook_profile_view, name='cook_profile_detail'),
    path('cook-meals/<int:cook_id>/', cook_meals_view, name='cook_meals_by_cook'),
    path('meal-details/<int:meal_id>/', meal_details_view, name='meal_detail_by_id'),
    path('my-meals/add/', add_meal_view, name='add_meal'),
    path('my-meals/<int:meal_id>/edit/', edit_meal_view, name="edit_meal",),
    path('my-meals/<int:meal_id>/toggle-availability/', toggle_meal_availability_view, name="toggle_meal_availability",),
]
