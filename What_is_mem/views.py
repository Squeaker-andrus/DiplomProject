import datetime
import json
import re
import os
import hashlib
import aiohttp_jinja2
from aiohttp import web
from aiohttp.web_request import Request
from aiohttp_session import Session
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.http import HttpResponseNotAllowed, HttpResponse
from .models import Rooms, Inventory, Rank, Suggestions
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password


def index_first_page(request):
    return render(request, 'first_pattern/first_page.html', {})


def show_rooms(request):
    all_rooms = Rooms.objects.all()
    return render(request, "second_pattern/main_page.html", {"rooms": all_rooms})

def show_users(request):
    all_users = User.objects.all()
    return render(request, "second_pattern/main_page.html", {"users": all_users})

def create_room(request):
    data = {}
    if request.method == "POST":
        title = request.POST.get("title", "")

        if title:
            tread = Rooms(title=title)
            tread.save()
            return redirect("main")

        data["title"] = title

    return render(request, "creation_room.html", data)

def room_view(request, room_id: int):
    room = Rooms.objects.get(id=room_id)
    return render(request, "room.html", {"post": room})

def update_room(request, tread_id: int):
    room = Rooms.objects.get(id=tread_id)

    if request.method == "POST":
        title = request.POST.get("title", "")
        if title:
            room.title = title
            room.save(update_fields=["title"])
            return redirect("view-room", room.id)


    return render(request, "edit_room.html", {"title": room.title, "room_id": room.id})

def delete_room(request, room_id: int):
    if request.method == "POST":
        Rooms.objects.get(id=room_id).delete()
        return redirect("main")
    return HttpResponseNotAllowed(permitted_methods=['POST'])
