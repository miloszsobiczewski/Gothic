# Generated by Django 2.2.1 on 2020-01-10 18:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("hepterakt", "0003_auto_20200107_1444"),
    ]

    operations = [
        migrations.CreateModel(
            name="Work",
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
                ("company", models.CharField(max_length=128)),
                ("money", models.CharField(blank=True, max_length=64, null=True)),
                ("url", models.URLField()),
                ("where", models.CharField(blank=True, max_length=32, null=True)),
                (
                    "application_date",
                    models.DateField(
                        default=datetime.datetime(2020, 1, 10, 18, 39, 47, 403793)
                    ),
                ),
                ("contact_date", models.DateField(blank=True, null=True)),
                ("status", models.CharField(default="applied", max_length=16)),
                ("note", models.TextField(blank=True, null=True)),
                ("applied_ind", models.BooleanField(default=True)),
            ],
        ),
        migrations.AlterField(
            model_name="timetracker",
            name="workday",
            field=models.DateField(
                default=datetime.datetime(2020, 1, 10, 18, 39, 47, 402812)
            ),
        ),
    ]