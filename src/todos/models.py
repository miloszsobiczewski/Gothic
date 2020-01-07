from django.db import models

todo = "todo"
in_progress = "in_progress"
done = "done"
SCORE = [(1, "very bad"), (2, "bad"), (3, "so so"), (4, "good"), (5, "very good")]
STATUS = [(todo, "To do"), (in_progress, "In progress"), (done, "Done")]


class Plan(models.Model):
    STATUS = [
        ("todo", "Todo"),
        ("in_progress", "In Progress"),
        ("hold", "On Hold"),
        ("done", "Done"),
        ("plan", "Plan"),
    ]
    group = models.CharField(max_length=64)
    status = models.CharField(choices=STATUS, max_length=64, default=todo)
    deadline = models.DateField(blank=True, null=True)
    task = models.CharField(max_length=256)
    comment = models.TextField(blank=True, null=True)


# todo : abstract this model
class Film(models.Model):
    title = models.CharField(max_length=128)
    author = models.CharField(max_length=128, null=True, blank=True)
    score = models.IntegerField(choices=SCORE, null=True, blank=True)
    comment = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=16, choices=STATUS, default=todo)
    date_added = models.DateField(auto_now_add=True)


class Book(models.Model):
    title = models.CharField(max_length=128)
    author = models.CharField(max_length=128, null=True, blank=True)
    score = models.IntegerField(choices=SCORE, null=True, blank=True)
    comment = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=16, choices=STATUS, default=todo)
    date_added = models.DateField(auto_now_add=True)
