# Generated by Django 3.2.13 on 2023-01-10 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bannerad", "0004_alter_bannerad_options"),
    ]

    operations = [
        migrations.AddField(
            model_name="bannerad",
            name="category",
            field=models.CharField(
                choices=[("mobile", "mobile"), ("web", "web")],
                default="web",
                max_length=10,
            ),
        ),
    ]
