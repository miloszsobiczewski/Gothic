# Generated by Django 2.2.1 on 2020-03-08 19:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("hepterakt", "0010_auto_20200307_1800")]

    operations = [
        migrations.AlterField(
            model_name="timetracker",
            name="workday",
            field=models.DateField(
                default=datetime.datetime(2020, 3, 8, 19, 55, 41, 928343)
            ),
        ),
        migrations.AlterField(
            model_name="work",
            name="application_date",
            field=models.DateField(
                default=datetime.datetime(2020, 3, 8, 19, 55, 41, 929026)
            ),
        ),
    ]
