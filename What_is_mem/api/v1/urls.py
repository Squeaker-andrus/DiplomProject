from django.urls import path
from . import views

# API V1

urlpatterns = [
    path("login/", views.login_user, name="log_in"),
    path("regist/", views.registrate_user, name="registrate_in"),
    path("logout/", views.logout_user, name="logout")
]