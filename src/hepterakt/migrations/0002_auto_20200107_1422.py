# Generated by Django 2.2.1 on 2020-01-07 14:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("hepterakt", "0001_initial")]

    operations = [
        migrations.AlterField(
            model_name="timetracker",
            name="timestamp",
            field=models.DateTimeField(
                default=datetime.datetime(2020, 1, 7, 14, 22, 16, 362471)
            ),
        )
    ]
