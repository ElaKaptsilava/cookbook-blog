# Generated by Django 5.0.4 on 2024-04-10 10:56

import django.db.models.deletion
import recipes_manager.models
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("recipes_manager", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Instruction",
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
                ("number", models.IntegerField()),
                ("description", models.TextField()),
                (
                    "file",
                    models.FileField(
                        blank=True,
                        null=True,
                        upload_to=recipes_manager.models.user_directory_path,
                    ),
                ),
                (
                    "recipe",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="recipes_manager.recipe",
                    ),
                ),
            ],
        ),
    ]
