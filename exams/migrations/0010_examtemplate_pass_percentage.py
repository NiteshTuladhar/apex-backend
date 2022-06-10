# Generated by Django 3.2.13 on 2022-06-08 07:54

from django.db import migrations

import common.modelFields


class Migration(migrations.Migration):

    dependencies = [
        ("exams", "0009_merge_20220603_1720"),
    ]

    operations = [
        migrations.AddField(
            model_name="examtemplate",
            name="pass_percentage",
            field=common.modelFields.PercentageField(
                decimal_places=2,
                default=0,
                max_digits=3,
                verbose_name="Pass Percentage",
            ),
            preserve_default=False,
        ),
    ]
