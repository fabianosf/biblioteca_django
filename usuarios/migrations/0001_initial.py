# Generated by Django 4.2.8 on 2023-12-12 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Usuario",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(max_length=30)),
                ("email", models.EmailField(max_length=254)),
                ("senha", models.CharField(max_length=64)),
            ],
        ),
    ]
