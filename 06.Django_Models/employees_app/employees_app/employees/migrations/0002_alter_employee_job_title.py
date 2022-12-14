# Generated by Django 4.1 on 2022-08-28 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("employees", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="employee",
            name="job_title",
            field=models.IntegerField(
                choices=[
                    (1, "Software developer"),
                    (2, "Data scientist"),
                    (5, "DevOps"),
                ],
                max_length=20,
            ),
        ),
    ]
