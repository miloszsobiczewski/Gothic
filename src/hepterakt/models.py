import datetime
import uuid
from django.db import models


class TimeTracker(models.Model):
    class Meta:
        verbose_name_plural = "Time Tracker"

    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    task = models.CharField(max_length=128)
    description = models.TextField()
    time_effort = models.DecimalField(max_digits=4, decimal_places=2)
    paid = models.BooleanField()
    workday = models.DateField(default=datetime.datetime.now())

    def __str__(self):
        return f"{self.workday} [{self.task}] {self.time_effort}"


class TimeSummary(TimeTracker):
    class Meta:
        proxy = True
        verbose_name = "Time Summary"
        verbose_name_plural = "Times Summary"


class Work(models.Model):
    position = models.CharField(max_length=128)
    company = models.CharField(max_length=128)
    money = models.CharField(max_length=64, blank=True, null=True)
    url = models.URLField()
    where = models.CharField(max_length=32, blank=True, null=True)
    application_date = models.DateField(default=datetime.datetime.now())
    contact_date = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=16, default="applied")
    note = models.TextField(blank=True, null=True)
    applied_ind = models.BooleanField(default=True)
    cv_version = models.CharField(max_length=16, blank=True, null=True)
    contact_ind = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.company} {self.position}"
