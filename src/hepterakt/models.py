import datetime
import uuid
from django.db import models


class TimeTracker(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    task = models.CharField(max_length=128)
    description = models.TextField()
    time_effort = models.DecimalField(max_digits=4, decimal_places=2)
    paid = models.BooleanField()
    workday = models.DateField(auto_now_add=True)


class TimeSummary(TimeTracker):
    class Meta:
        proxy = True
        verbose_name = "Time Summary"
        verbose_name_plural = "Times Summary"
