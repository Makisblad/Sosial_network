# Generated by Django 4.1.1 on 2022-10-18 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app_users", "0004_alter_user_slug_alter_user_username"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="username",
            field=models.CharField(max_length=30, unique=True, verbose_name="Ник"),
        ),
    ]