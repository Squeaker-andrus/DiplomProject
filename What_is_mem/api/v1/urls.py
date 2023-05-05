from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LoginView
from . import views

# API V1

urlpatterns = [
    path("login/", views.login_user, name="log_in"),
    path("regist/", views.registrate_user, name="registrate_in")
]