# Generated by Django 2.2.4 on 2020-04-04 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("things", "0001_initial")]

    operations = [
        migrations.AddField(
            model_name="thing", name="bought", field=models.BooleanField(default=False)
        )
    ]
