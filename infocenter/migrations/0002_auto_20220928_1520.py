# Generated by Django 3.2.13 on 2022-09-28 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("infocenter", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="courseinfo",
            name="colleges",
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name="courseinfo",
            name="eligibility",
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name="courseinfo",
            name="introduction",
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name="courseinfo",
            name="syllabus",
            field=models.TextField(blank=True),
        ),
    ]