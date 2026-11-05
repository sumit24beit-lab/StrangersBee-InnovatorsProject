from django.urls import path

from . import views

urlpatterns = [
    path("", views.landing_page_view, name="landing"),
    path("about/", views.about_page_view, name="about"),
]