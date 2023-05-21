from django.shortcuts import render, redirect
from .forms import UserInfo
from ...models import Player
from django.views.generic import UpdateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.http import HttpResponse, HttpResponseForbidden
from django.contrib.auth.models import User


def player_info(request):
    all_info = Player.objects.get(user_id=request.session.get('_auth_user_id'))
    return render(request, "second_pattern/user_profile.html", {"player_info": all_info})


# class ProfileUpdateView(LoginRequiredMixin, UpdateView):
#     model = Player
#     form_class = UserInfo
#     template_name = 'second_pattern/user_profile_settings.html'
#     success_url = reverse_lazy('show_profile')
#
#     def get_object(self):
#         print(self.request.POST)
#         return self.request.user.player
#
#     def form_valid(self, form):
#         if form.instance.user != self.request.user:
#             return HttpResponseForbidden()
#         return super().form_valid(form)


def update_profile(request):
    print(request.user.player)
    data = Player.objects.get(id=request.session.get('_auth_user_id'))
    print(request.POST)
    print(data)
    if request.method == "POST":
        print("check1....................")
        first_name = request.POST.get("first_name", "")
        last_name = request.POST.get("last_name", "")
        user_pick = request.FILES.get("user_pick")
        country = request.POST.get("country", "")
        age = request.POST.get("age", "")
        email = request.POST.get("email", "")
        about = request.POST.get("about", "")
        print("check2.........................")
        print(first_name, last_name, country, age, email, about)
        if first_name and last_name and user_pick and country and age and email and about:
            data.first_name = first_name
            data.last_name = last_name
            data.user_pick = user_pick
            data.country = country
            data.age = age
            data.email = email
            data.about = about
            data.save()
            print('check3..................')
            return redirect("show_profile")
    print("check4.....................")
    return render(request, "second_pattern/user_profile_settings.html", {"first_name": data.first_name,
                                                                "last_name": data.last_name,
                                                                "user_pick": data.user_pick,
                                                                "country": data.country,
                                                                "age": data.age,
                                                                "email": data.email,
                                                                "about": data.about
                                                                }
                  )