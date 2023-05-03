import datetime
import aiohttp_jinja2
from django.http import HttpResponse
from aiohttp import web
from django.views import View
from .serializers import UserLoginSerialize
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from . import forms
from django.contrib.auth.forms import UserCreationForm
from django.views import generic
from django.urls import reverse_lazy

""" 
API V1 
"""


def encrypt_password(password):
    hashed_password = make_password(password)
    return hashed_password


# def login_user(request):
#     if request.method == "GET":
#         return redirect(request, "first_pattern/sign-in.html")
#     elif request.method == "POST":
#         data = request.post()
#         username = data.get('inputusername', '')
#         password = encrypt_password(data.get('inputpassword', ''))
#         try:
#             user = User.objects.get(username=username)
#         except Exception as error:
#             print(error)
#
#             return redirect(request, "first_pattern/sign-in.html")
#         else:
#             if user.is_active and password != User.objects.get(password):
#                 redirect(request, "second_pattern/main_page.html")
#             else:
#                 login(user)
#             return HttpResponse({"user": user.id})

class SignIn(generic.CreateView):
    form_class = UserCreationForm
    template_name = "first_pattern/sign-in.html"
    success_url = reverse_lazy("home")

    def saver(self):
        username = self.request.POST.get("inputusername", "")
        password = encrypt_password(self.request.POST.get("inputpassword", ""))
        if username and password:
            user = User(username=username, password=password)
            user.save()
            return redirect("home")


