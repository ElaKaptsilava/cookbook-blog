# Generated by Django 5.0.4 on 2024-04-11 09:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("recipes_manager", "0002_instruction"),
        ("reviews_ratings", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="CommunityOpinion",
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
                (
                    "email",
                    models.EmailField(
                        help_text="Your email address.", max_length=254, unique=True
                    ),
                ),
                (
                    "first_name",
                    models.CharField(help_text="Your first name.", max_length=50),
                ),
                (
                    "last_name",
                    models.CharField(help_text="Your last name.", max_length=50),
                ),
                (
                    "opinion",
                    models.TextField(help_text="Your opinion about the recipe."),
                ),
                (
                    "date",
                    models.DateField(
                        auto_now_add=True, help_text="Date when the opinion was added."
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
            options={
                "unique_together": {("email", "recipe")},
            },
        ),
    ]
