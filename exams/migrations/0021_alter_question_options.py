# Generated by Django 3.2.13 on 2022-07-04 12:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("exams", "0020_alter_question_section"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="question",
            options={
                "ordering": ["exam", "section", "id"],
                "verbose_name": "Question",
                "verbose_name_plural": "Questions",
            },
        ),
    ]
