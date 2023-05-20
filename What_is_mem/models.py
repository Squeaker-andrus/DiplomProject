from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

class Rooms(models.Model):
    title = models.TextField()
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="creator", null=False)
    include_users = models.ForeignKey(User, on_delete=models.CASCADE, related_name="includers", null=True)
    created = models.DateTimeField(default=datetime.now())

class Inventory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    itemname = models.TextField()
    quantity = models.BigIntegerField(null=True)

class SpecialCards(models.Model):
    itemname = models.TextField()
    visual = models.ImageField()


class Questions(models.Model):
    question = models.TextField

class Cards(models.Model):
    cardname = models.TextField()
    card = models.ImageField()

class Rank(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rank = models.PositiveIntegerField(default=0)

class Suggestions(models.Model):
    sug_user = models.ForeignKey(User, on_delete=models.CASCADE)
    suggestion = models.TextField(max_length=400)
