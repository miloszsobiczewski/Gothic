# Generated by Django 2.2.1 on 2020-01-10 19:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("hobby", "0006_auto_20200110_1839"),
    ]

    operations = [
        migrations.AlterField(
            model_name="jeep",
            name="date",
            field=models.DateField(
                default=datetime.datetime(2020, 1, 10, 19, 14, 28, 820645)
            ),
        ),
        migrations.AlterField(
            model_name="shooting",
            name="date",
            field=models.DateField(
                default=datetime.datetime(2020, 1, 10, 19, 14, 28, 821397)
            ),
        ),
    ]
