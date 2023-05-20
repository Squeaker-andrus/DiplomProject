from django.shortcuts import render, redirect
from django.http import HttpResponseNotAllowed
from What_is_mem.models import Rooms
from datetime import datetime
from django.contrib.auth.models import User


def show_all_rooms(request):
    all_rooms = Rooms.objects.all()
    return render(request, "second_pattern/rooms_page.html", {"rooms": all_rooms})


def show_my_rooms(request):
    my_rooms = Rooms.objects.filter(creator=User(id=request.session.get('_auth_user_id')))
    return render(request, "second_pattern/my_rooms.html", {"rooms": my_rooms})


def create_room(request):
    data = {}
    if request.method == "POST":
        title = request.POST.get("title", "")
        creator = request.session.get('_auth_user_id')
        if title:
            room = Rooms(creator=User(id=creator), title=title, created=datetime.now())
            room.save()
            return redirect("rooms")

        data["title"] = title

    return render(request, "second_pattern/creation_room.html", data)


def room_view(request, room_id: int):
    room = Rooms.objects.get(id=room_id)
    return render(request, "second_pattern/room.html", {"room": room})


def update_room(request, room_id: int):
    room = Rooms.objects.get(id=room_id)
    if request.method == "POST":
        title = request.POST.get("title", "")
        if title:
            room.title = title
            room.save(update_fields=["title"])
            return redirect("room", room.id)

    return render(request, "second_pattern/upgrade_room.html", {"title": room.title, "room_id": room.id})


def delete_room(request, room_id: int):
    if request.method == "POST":
        Rooms.objects.get(id=room_id).delete()
        return redirect("my_rooms")
    return HttpResponseNotAllowed(permitted_methods=['POST'])
