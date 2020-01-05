from django.db import models


SCORE = [(1, "very bad"), (2, "bad"), (3, "so so"), (4, "good"), (5, "very good")]
STATUS = [("tod_do", "To do"), ("in_progress", "In progress"), ("done", "Done")]


class Plan(models.Model):
    STATUS = [
        ("todo", "Todo"),
        ("in_progress", "In Progress"),
        ("hold", "On Hold"),
        ("done", "Done"),
        ("plan", "Plan"),
    ]
    group = models.CharField(max_length=64)
    status = models.CharField(choices=STATUS, max_length=64)
    deadline = models.DateField(blank=True, null=True)
    task = models.CharField(max_length=256)
    comment = models.TextField(blank=True, null=True)


class Film(models.Model):
    title = models.CharField(max_length=128)
    score = models.IntegerField(choices=SCORE, null=True, blank=True)
    comment = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=16, choices=STATUS)
    date_added = models.DateField(auto_now_add=True)


class Book(models.Model):
    title = models.CharField(max_length=128)
    score = models.IntegerField(choices=SCORE, null=True, blank=True)
    comment = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=16, choices=STATUS)
    date_added = models.DateField(auto_now_add=True)
