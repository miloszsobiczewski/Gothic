# Generated by Django 2.2.1 on 2020-03-12 19:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hepterakt', '0011_auto_20200308_1955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timetracker',
            name='workday',
            field=models.DateField(default=datetime.datetime(2020, 3, 12, 19, 56, 55, 299249)),
        ),
        migrations.AlterField(
            model_name='work',
            name='application_date',
            field=models.DateField(default=datetime.datetime(2020, 3, 12, 19, 56, 55, 300150)),
        ),
    ]
