from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


class Player(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.TextField(null=False, default="Player_first_name", max_length=255)
    last_name = models.TextField(null=False, default="Player_last_name", max_length=255)
    user_pick = models.ImageField(null=True,
                                  blank=True,
                                  upload_to="media/custom",
                                  default="media/default/200px-Wojak.png")
    country = models.TextField(null=True)
    age = models.IntegerField(null=True)
    email = models.EmailField(null=True)
    about = models.TextField(null=True, max_length=255)

    def __str__(self):
        return str(self.user_id)

