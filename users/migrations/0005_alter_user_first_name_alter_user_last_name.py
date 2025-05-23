# Generated by Django 5.1.7 on 2025-04-02 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0004_remove_user_role"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="first_name",
            field=models.CharField(
                blank=True, help_text="Укажите ваше имя", max_length=30, null=True
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="last_name",
            field=models.CharField(
                blank=True, help_text="Укажите вашу фамилию", max_length=30, null=True
            ),
        ),
    ]
