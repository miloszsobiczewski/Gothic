# Generated by Django 2.2.1 on 2020-03-07 15:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("hobby", "0010_auto_20200223_2131"),
    ]

    operations = [
        migrations.AlterField(
            model_name="jeep",
            name="date",
            field=models.DateField(
                default=datetime.datetime(2020, 3, 7, 15, 35, 23, 573820)
            ),
        ),
        migrations.AlterField(
            model_name="shooting",
            name="date",
            field=models.DateField(
                default=datetime.datetime(2020, 3, 7, 15, 35, 23, 574335)
            ),
        ),
    ]
