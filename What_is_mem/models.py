from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

class Rooms(models.Model):
    title = models.TextField()
    unclude_users = User.username
    created = models.DateTimeField(default=datetime.now())

class Inventory(models.Model):
    user = User.username
    itemname = models.TextField()
    quantity = models.BigIntegerField(null=True)

class SpecialCards(models.Model):
    itemname = models.TextField
    visual = models.ImageField()


class Questions(models.Model):
    question = models.TextField

class Cards(models.Model):
    cardname = models.TextField
    card = models.ImageField()

class Rank(models.Model):
    user = User.username
    rank = models.PositiveIntegerField(default=0)

class Suggestions(models.Model):
    sug_user = User.username
    suggestion = models.TextField(max_length=400)
