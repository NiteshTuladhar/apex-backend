# Generated by Django 3.2.13 on 2022-06-08 08:09

from decimal import Decimal

import django.db.models.deletion
from django.db import migrations, models

import common.modelFields


class Migration(migrations.Migration):

    dependencies = [
        ("exams", "0012_auto_20220608_1350"),
    ]

    operations = [
        migrations.AddField(
            model_name="section",
            name="neg_percentage",
            field=common.modelFields.PercentageField(
                decimal_places=2,
                default=0,
                help_text="Enter value between 0 and 1.",
                max_digits=3,
                verbose_name="Negative Percentage",
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="section",
            name="name",
            field=models.CharField(max_length=64, verbose_name="Name"),
        ),
        migrations.AlterField(
            model_name="section",
            name="neg_marks",
            field=models.DecimalField(
                decimal_places=2,
                default=Decimal("0.4"),
                max_digits=5,
                verbose_name="Negative Marks",
            ),
        ),
        migrations.AlterField(
            model_name="section",
            name="num_of_questions",
            field=models.IntegerField(default=0, verbose_name="Number Of Questions"),
        ),
        migrations.AlterField(
            model_name="section",
            name="pos_marks",
            field=models.DecimalField(
                decimal_places=2,
                default=Decimal("2.0"),
                max_digits=5,
                verbose_name="Positive Marks",
            ),
        ),
        migrations.AlterField(
            model_name="section",
            name="template",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="exams.examtemplate",
                verbose_name="Template",
            ),
        ),
    ]