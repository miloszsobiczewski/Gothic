from django.db import models


class Thing(models.Model):
    thing = models.CharField(max_length=128)
    date = models.DateField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    approved = models.BooleanField(default=False)
    bought = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.thing}"


class Warranty(models.Model):
    thing = models.CharField(max_length=128)
    start_date = models.DateField()
    end_date = models.DateField()
    receipt = models.FileField()

    def __str__(self):
        return f"{self.thing}"
