from django.db import models
from datetime import date
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User

class Restaurant(models.Model):
    google_place_id = models.CharField(max_length=250)
    name = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    def __str__(self):
        return self.name

class Menu(models.Model):
    menu_photo_url = models.CharField(max_length=200)
    approved = models.BooleanField(default=False)
    pending = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    def __str__(self):
        return self.menu_photo_url

class MenuVote(models.Model):
    vote = models.BooleanField(default=True)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.user)
    
class Hours(models.Model):
    hours = models.CharField(max_length=200)
    approved = models.BooleanField(default=False)
    pending = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    def __str__(self):
        return self.hours

class HoursVote(models.Model):
    vote = models.BooleanField(default=True)
    hours = models.ForeignKey(Hours, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.user)