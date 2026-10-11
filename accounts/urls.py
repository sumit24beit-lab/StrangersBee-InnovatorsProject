from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='accounts_login'),
    path('signup/', views.signup_view, name='accounts_signup'),
]