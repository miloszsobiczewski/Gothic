# Generated by Django 2.2.1 on 2020-01-07 14:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("hobby", "0002_auto_20200107_1406"),
    ]

    operations = [
        migrations.AlterField(
            model_name="jeep",
            name="date",
            field=models.DateField(
                default=datetime.datetime(2020, 1, 7, 14, 6, 56, 111289)
            ),
        ),
        migrations.AlterField(
            model_name="shooting",
            name="date",
            field=models.DateField(
                default=datetime.datetime(2020, 1, 7, 14, 6, 56, 111815)
            ),
        ),
    ]