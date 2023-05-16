from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from .forms import UserRegistration
from Costomise.models import Player
from django.contrib.auth.forms import AuthenticationForm


""" 
WIM API V1 
"""


def encrypt_password(password):
    hashed_password = make_password(password)
    return hashed_password


def login_user(request):
    if request.method == "GET":
        form = AuthenticationForm()
        return render(request, "first_pattern/sign-in.html", {"form": form})
    elif request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("home")
            else:
                return render(request, "first_pattern/sign-in.html", {"form": form, "error": "Неправильный пользователь или пароль"})
        else:
            return render(request, "first_pattern/sign-in.html", {"form": form, "error": "Неправильный пользователь или пароль"})


def registrate_user(request):
    if request.method == "GET":
        form = UserRegistration()
        return render(request, "first_pattern/registrate.html", {"form": form})
    elif request.method == "POST":
        form = UserRegistration(request.POST)
        if form.is_valid():
            user = form.save()
            player = Player(user_id=user)
            player.save()
            if user is not None:
                login(request, user)
                return redirect("home")
            else:
                return render(request, "first_pattern/registrate.html", {"form": form, "error": "User creation failed"})
        else:
            print(form.errors)
            return render(request, "first_pattern/registrate.html", {"form": form})


def logout_user(request):
    logout(request)
    return redirect("basic")
