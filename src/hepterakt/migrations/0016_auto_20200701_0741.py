# Generated by Django 2.2.4 on 2020-07-01 07:41

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [("hepterakt", "0015_auto_20200614_1924")]

    operations = [
        migrations.AlterField(
            model_name="timetracker",
            name="workday",
            field=models.DateField(
                default=datetime.datetime(2020, 7, 1, 7, 41, 9, 921367, tzinfo=utc)
            ),
        ),
        migrations.AlterField(
            model_name="work",
            name="application_date",
            field=models.DateField(
                default=datetime.datetime(2020, 7, 1, 7, 41, 9, 922401, tzinfo=utc)
            ),
        ),
    ]
