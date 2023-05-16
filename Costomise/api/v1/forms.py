from django import forms
from django.forms import ModelForm
from ...models import Player


class UserInfo(ModelForm):

    class Meta:
        model = Player
        fields = ["first_name", "last_name", "user_pick", "country", "age", "email", "about"]
