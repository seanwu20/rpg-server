from django.db import models
from django.contrib.auth.models import User


class UserData(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    user_food = models.IntegerField()
    user_water = models.IntegerField()
    state = models.CharField(max_length=30, blank=False)
    city = models.CharField(max_length=30, blank=False)
    location = models.CharField(max_length=30, blank=False)
    food_available_1 = models.IntegerField(blank=False)
    water_available_1 = models.IntegerField(blank=False)
    location_2 = models.CharField(max_length=30, blank=False)
    food_available_2 = models.IntegerField(blank=False)
    water_available_2 = models.IntegerField(blank=False)
