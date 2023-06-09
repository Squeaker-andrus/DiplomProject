"""
URL configuration for Project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from What_is_mem import views

urlpatterns = [
   path('admin/', admin.site.urls, name="admin_page"),
   path('', views.index_first_page, name="basic"),
   path('api/v1/', include("What_is_mem.api.v1.urls")),
   path('home/', views.show_rooms, name="home"),
   path('profile/', include("Costomise.api.v1.urls")),
   path('rooms/', include("GameRooms.api.v1.urls")),
   # path('person/', name="private_page"),

]
