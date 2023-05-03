from rest_framework import serializers
from django.contrib.auth.models import User

class UserLoginSerialize(serializers.ModelSerializer):

    class Meta():
        model = User
        field = ["id", "username", "password"]