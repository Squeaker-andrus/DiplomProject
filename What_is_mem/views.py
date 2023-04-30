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
from django.http import HttpResponseNotAllowed
from .models import Rooms, Inventory, Rank, Suggestions
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

async def encrypt_password(password):
    hashed_password = make_password(password)
    return hashed_password


class LogIn(web.View):

    @aiohttp_jinja2.template("users/login.html")
    async def login(self, request):
        if request.method == 'GET':
            return {}
        elif request.method == 'POST':
            data = await request.post()
            username = data.get('username')
            password = encrypt_password(data.get('password'))
            user = authenticate(request, username=username, password=password)
            if user is not None and user.is_active:
                login(request, user)
                return redirect('/')
            else:
                return {'error': 'Неверное имя пользователя или пароль'}


class Register(web.View):

    @aiohttp_jinja2.template("users/register.html")
    async def register(self, request):
        if request.method == 'GET':
            return {}
        elif request.method == 'POST':
            data = await request.post()
            username = data.get('username', '').lower()
            row_password = data.get('password', '')
            if not re.match(r'^[a-z]\w{0,9}$', username) and not re.match(r'^[a-z]\w{0,9}$', row_password):
                return ""
            else:
                password = await encrypt_password(row_password)
                await User.save(username=username, password=password)
                login(request, User(username=username))
                return redirect('/')


class Logout(web.View):
    pass
    #@login_required
    #async def get(self):
    #    self.request.session.pop("user_id")
    #    redirect(self.request, "home")


def show_rooms(request):
    all_rooms = Rooms.objects.all()
    return render(request, "main_page.html", {"rooms": all_rooms})

def show_users(request):
    all_users = User.objects.all()
    return render(request, "main_page.html", {"users": all_users})

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
