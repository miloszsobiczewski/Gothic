# Generated by Django 2.2.1 on 2020-01-07 14:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("hobby", "0004_auto_20200107_1422")]

    operations = [
        migrations.AlterField(
            model_name="jeep",
            name="date",
            field=models.DateField(
                default=datetime.datetime(2020, 1, 7, 14, 44, 33, 113218)
            ),
        ),
        migrations.AlterField(
            model_name="shooting",
            name="date",
            field=models.DateField(
                default=datetime.datetime(2020, 1, 7, 14, 44, 33, 113707)
            ),
        ),
    ]
