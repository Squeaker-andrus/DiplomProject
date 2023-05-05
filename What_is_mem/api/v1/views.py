from datetime import datetime
import aiohttp_jinja2
from django.http import HttpResponse
from aiohttp import web
from django.views import View
from .serializers import UserLoginSerialize
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from django.contrib.auth.views import LoginView, FormView
from .forms import UserRegistration, UserLoginForm
from django.contrib.auth.forms import UserCreationForm
from django.views import generic
from django.urls import reverse_lazy

""" 
API V1 
"""


def encrypt_password(password):
    hashed_password = make_password(password)
    return hashed_password


def login_user(request):
    if request.method == "GET":
        form = UserLoginForm()
        return render(request, "first_pattern/sign-in.html", {"form": form})
    elif request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("home")
            else:
                return render(request, "first_pattern/sign-in.html", {"form": form, "error": "Неправильный пользователь или пароль"})
        else:
            return render(request, "first_pattern/sign-in.html", {"form": form})


def registrate_user(request):
    if request.method == "GET":
        form = UserRegistration()
        return render(request, "first_pattern/registrate.html", {"form": form})
    elif request.method == "POST":
        form = UserRegistration(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = User.objects.create_user(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("home")
            else:
                return render(request, "first_pattern/registrate.html", {"form": form, "error": "User creation failed"})
        else:
            return render(request, "first_pattern/registrate.html", {"form": form})



# class SignIn(generic.CreateView):
#     form_class = UserCreationForm
#     template_name = "first_pattern/sign-in.html"
#     success_url = reverse_lazy("home")
#
#     def saver(self):
#         username = self.request.POST.get("inputusername", "")
#         password = encrypt_password(self.request.POST.get("inputpassword", ""))
#         if username and password:
#             user = User(username=username, password=password)
#             user.save()
#             return redirect("home")


# class LogIn(View):
#
#     def get(self):
#         return {}
#
#     def post(self):
#         data = self.request.POST()
#         username = data.get('inputusername', '')
#         password = encrypt_password(data.get('inputpassword', ''))
#         try:
#             user = User.objects.get(username=username)
#
#         except Exception as error:
#             print(error)
#             redirect(self.request, "log_in")
#             return
#
#         else:
#             if User.objects.get[password] != password:
#                 redirect(self.request, "log_in")
#             else:
#                 self.login(user)
#         return HttpResponse({"user": user.id})
#
#     def login(self, user: User):
#
#         self.request.session["user_id"] = user.id
#         self.request.session["time"] = str(datetime.now())
#
#         redirect(self.request, "home")

# class Register(View):
#
#     def get(self):
#         return {}
#
#     def login(self, user: User):
#         self.request.session["user_id"] = user.id
#         self.request.session["time"] = str(datetime.now())
#
#         redirect(self.request, "home")
#
#     def post(self):
#         data = self.request.POST()
#         username = data.get('inputusername', '')
#         password = encrypt_password(data.get('inputpassword', ''))
#         print('username', username, password)
#
#         if not username or not password:
#             redirect(self.request, "registrate_in")
#
#         try:
#             User.objects.get(username=username)
#             redirect(self.request, "log_in")
#         except:
#             print("Пользователя нет!")
#
#         User.objects.create(username=username, password=password)
#         user = User.objects.get(username=username, password=password)
#
#         self.login(user)
