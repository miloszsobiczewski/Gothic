# Generated by Django 2.2.1 on 2020-01-10 18:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("hobby", "0005_auto_20200107_1444"),
    ]

    operations = [
        migrations.AlterField(
            model_name="jeep",
            name="date",
            field=models.DateField(
                default=datetime.datetime(2020, 1, 10, 18, 39, 47, 400014)
            ),
        ),
        migrations.AlterField(
            model_name="shooting",
            name="date",
            field=models.DateField(
                default=datetime.datetime(2020, 1, 10, 18, 39, 47, 400549)
            ),
        ),
    ]
