from django.urls import path
from . import views


# GR api v1

urlpatterns = [
    path("room/<int:room_id>", views.room_view, name="room"),
    path("", views.show_all_rooms, name="rooms"),
    path("my_rooms/", views.show_my_rooms, name="my_rooms"),
    path("create_room/", views.create_room, name="create_room"),
    path("update_room/<int:room_id>", views.update_room, name="update_room"),
    path("delete/<int:room_id>", views.delete_room, name="delete_room")
]