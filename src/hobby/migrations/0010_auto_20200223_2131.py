# Generated by Django 2.2.1 on 2020-02-23 21:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hobby', '0009_auto_20200110_1939'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='jeep',
            options={'verbose_name_plural': 'Jeep'},
        ),
        migrations.AlterModelOptions(
            name='shooting',
            options={'verbose_name_plural': 'Shooting'},
        ),
        migrations.AlterField(
            model_name='jeep',
            name='date',
            field=models.DateField(default=datetime.datetime(2020, 2, 23, 21, 31, 24, 900726)),
        ),
        migrations.AlterField(
            model_name='shooting',
            name='date',
            field=models.DateField(default=datetime.datetime(2020, 2, 23, 21, 31, 24, 901509)),
        ),
    ]