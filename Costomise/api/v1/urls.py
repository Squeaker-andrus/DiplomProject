from django.urls import path
from . import views


# Costomise api v1

urlpatterns = [
    path("settings/", views.update_profile, name="update_profile"),
    path("", views.player_info, name="show_profile"),
    # path("logout/", views.logout_user, name="logout")
]
