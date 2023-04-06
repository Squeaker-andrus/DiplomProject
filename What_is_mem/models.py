from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

class Rooms(models.Model):
    title = models.TextField()
    unclude_users = User.username
    created = models.DateTimeField(default=datetime.now())

class Inventory(models.Model):
    user = User.username
    items = models.BigAutoField(null=True)

class Questions(models.Model):
    question = models.TextField

class Cards(models.Model):
    card = models.ImageField()

class Rank(models.Model):
    user = User.username
    rank = models.PositiveIntegerField(default=0)

class Suggestions(models.Model):
    sug_user = User.username
    suggestion = models.TextField(max_length=400)
