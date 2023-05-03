from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LoginView
from . import views

# API V1

urlpatterns = [
    path("login/", views.SignIn.as_view(), name="login"),
    path("regist/", LoginView.as_view(template_name="first_pattern/registrate.html"), name="registrate")
]