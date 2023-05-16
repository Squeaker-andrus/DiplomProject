from django.shortcuts import render, redirect
from .forms import UserInfo
from ...models import Player
from django.views.generic import UpdateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.http import HttpResponse, HttpResponseForbidden





def player_info(request):
    all_info = Player.objects.get(user_id=request.session.get('_auth_user_id'))
    return render(request, "second_pattern/user_profile.html", {"player_info": all_info})

class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Player
    form_class = UserInfo
    template_name = 'second_pattern/user_profile_settings.html'
    success_url = reverse_lazy('show_profile')

    def get_object(self):
        print(self.request.POST)
        return self.request.user

    def form_valid(self, form):
        if form.instance.user != self.request.user:
            return HttpResponseForbidden()
        return super().form_valid(form)
