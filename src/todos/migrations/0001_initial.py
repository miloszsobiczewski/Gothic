# Generated by Django 2.2.1 on 2020-01-05 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Film",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=128)),
                (
                    "score",
                    models.IntegerField(
                        blank=True,
                        choices=[
                            (1, "very bad"),
                            (2, "bad"),
                            (3, "so so"),
                            (4, "good"),
                            (5, "very good"),
                        ],
                        null=True,
                    ),
                ),
                ("comment", models.TextField(blank=True, null=True)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("tod_do", "To do"),
                            ("in_progress", "In progress"),
                            ("done", "Done"),
                        ],
                        max_length=16,
                    ),
                ),
                ("date_added", models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="Plan",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("group", models.CharField(max_length=64)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("todo", "Todo"),
                            ("in_progress", "In Progress"),
                            ("hold", "On Hold"),
                            ("done", "Done"),
                            ("plan", "Plan"),
                        ],
                        max_length=64,
                    ),
                ),
                ("deadline", models.DateField(blank=True, null=True)),
                ("task", models.CharField(max_length=256)),
                ("comment", models.TextField(blank=True, null=True)),
            ],
        ),
    ]
