# Generated by Django 4.1.1 on 2022-10-18 10:40

import autoslug.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app_users", "0003_user_username_alter_user_birth_date_alter_user_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="slug",
            field=autoslug.fields.AutoSlugField(
                editable=False, populate_from="username", verbose_name="slug"
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="username",
            field=models.CharField(
                blank=True, max_length=30, unique=True, verbose_name="Ник"
            ),
        ),
    ]
