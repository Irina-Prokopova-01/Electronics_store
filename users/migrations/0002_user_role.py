# Generated by Django 5.1.7 on 2025-03-28 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="role",
            field=models.CharField(
                choices=[("user", "User"), ("admin", "Admin")],
                default="user",
                max_length=20,
            ),
        ),
    ]
