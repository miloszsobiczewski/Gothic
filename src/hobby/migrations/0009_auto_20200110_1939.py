# Generated by Django 2.2.1 on 2020-01-10 19:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("hobby", "0008_auto_20200110_1939"),
    ]

    operations = [
        migrations.AlterField(
            model_name="jeep",
            name="date",
            field=models.DateField(
                default=datetime.datetime(2020, 1, 10, 19, 39, 46, 287413)
            ),
        ),
        migrations.AlterField(
            model_name="shooting",
            name="date",
            field=models.DateField(
                default=datetime.datetime(2020, 1, 10, 19, 39, 46, 287935)
            ),
        ),
    ]