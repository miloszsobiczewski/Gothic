# Generated by Django 2.2.1 on 2020-01-07 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("todos", "0002_book"),
    ]

    operations = [
        migrations.AddField(
            model_name="book",
            name="author",
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AddField(
            model_name="film",
            name="author",
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name="book",
            name="status",
            field=models.CharField(
                choices=[
                    ("todo", "To do"),
                    ("in_progress", "In progress"),
                    ("done", "Done"),
                ],
                default="todo",
                max_length=16,
            ),
        ),
        migrations.AlterField(
            model_name="film",
            name="status",
            field=models.CharField(
                choices=[
                    ("todo", "To do"),
                    ("in_progress", "In progress"),
                    ("done", "Done"),
                ],
                default="todo",
                max_length=16,
            ),
        ),
        migrations.AlterField(
            model_name="plan",
            name="status",
            field=models.CharField(
                choices=[
                    ("todo", "Todo"),
                    ("in_progress", "In Progress"),
                    ("hold", "On Hold"),
                    ("done", "Done"),
                    ("plan", "Plan"),
                ],
                default="todo",
                max_length=64,
            ),
        ),
    ]