import datetime

from django.db import models


class Jeep(models.Model):
    miledge = models.PositiveIntegerField()
    task = models.CharField(max_length=128)
    date = models.DateField(default=datetime.datetime.today())
    mechanic = models.CharField(max_length=32, default="Miłosz")
    parts_price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    labor_price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    details = models.TextField(null=True, blank=True)
    done = models.BooleanField(default=True)

    def __str__(self):
        return self.task


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
