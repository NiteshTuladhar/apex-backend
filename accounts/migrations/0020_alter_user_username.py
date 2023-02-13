# Generated by Django 3.2.13 on 2023-01-20 05:04

from django.db import migrations, models

import accounts.validators


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0019_alter_profile_interests"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="username",
            field=models.CharField(
                db_index=True,
                error_messages={"unique": "A user with that phone already exists."},
                help_text="Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.",
                max_length=150,
                unique=True,
                validators=[accounts.validators.PhoneNumberValidator()],
                verbose_name="username",
            ),
        ),
    ]