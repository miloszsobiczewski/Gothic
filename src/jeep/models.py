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
