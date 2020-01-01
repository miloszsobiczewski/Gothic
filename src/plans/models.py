from django.db import models


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
