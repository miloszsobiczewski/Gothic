# Generated by Django 2.2.1 on 2020-01-07 14:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("hobby", "0003_auto_20200107_1406")]

    operations = [
        migrations.AlterField(
            model_name="jeep",
            name="date",
            field=models.DateField(
                default=datetime.datetime(2020, 1, 7, 14, 22, 16, 356514)
            ),
        ),
        migrations.AlterField(
            model_name="shooting",
            name="date",
            field=models.DateField(
                default=datetime.datetime(2020, 1, 7, 14, 22, 16, 357110)
            ),
        ),
    ]
