# Generated by Django 3.2.13 on 2022-06-27 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "attendance",
            "0004_rename_number_of_peroid_teacherattendancedetail_number_of_period",
        ),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="teacherattendance",
            options={"ordering": ["name"]},
        ),
        migrations.AddField(
            model_name="teacherattendance",
            name="name",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]