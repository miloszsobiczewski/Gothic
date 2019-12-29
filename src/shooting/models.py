import datetime

from django.db import models


class Shooting(models.Model):
    CATEGORY = [
        ("pistol", "Pistolet"),
        ("rifle", "Karabin"),
        ("gun", "Strzelba"),
    ]
    category = models.CharField(choices=CATEGORY, max_length=16)
    year = models.PositiveIntegerField(default=2020)
    date = models.DateField(default=datetime.datetime.today())
    place = models.CharField(max_length=128)
    competition = models.CharField(max_length=32)
    score = models.CharField(max_length=32, null=True, blank=True)
    confirmation = models.FileField(blank=True, null=True, upload_to="shooting/%Y")
    done = models.BooleanField(default=True)
