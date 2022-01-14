from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.search_user, name="search_url"),
    path('help', views.help, name="help_url"),
    path('contact', views.contact_me, name="contact_url")
]
