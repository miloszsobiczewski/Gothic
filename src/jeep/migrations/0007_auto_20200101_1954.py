# Generated by Django 2.2.1 on 2020-01-01 19:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("jeep", "0006_auto_20191229_2224"),
    ]

    operations = [
        migrations.AlterField(
            model_name="jeep",
            name="date",
            field=models.DateField(
                default=datetime.datetime(2020, 1, 1, 19, 54, 6, 511278)
            ),
        ),
    ]
