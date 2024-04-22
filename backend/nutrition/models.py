from django.db import models


class Ingredient(models.Model):
    name = models.CharField(max_length=256, help_text="Name of the ingredient.")
    serving_size_g = models.FloatField(help_text="Serving size in grams.")
    calories = models.FloatField(help_text="Calories per serving.")
    protein_g = models.FloatField(help_text="Protein content per serving in grams.")
    sugar_g = models.FloatField(help_text="Sugar content per serving in grams.")
    fat_total_g = models.FloatField(help_text="Total fat content per serving in grams.")
    carbohydrates_total_g = models.FloatField(null=True, blank=True, help_text="Total carbohydrates per serving in grams.")
    cholesterol_mg = models.FloatField(help_text="Cholesterol content per serving in milligrams.")
    potassium_mg = models.FloatField(null=True, blank=True, help_text="Potassium content per serving in milligrams.")
    sodium_mg = models.FloatField(null=True, blank=True, help_text="Sodium content per serving in milligrams.")
    fiber_g = models.FloatField(null=True, blank=True, help_text="Fiber content per serving in grams.")

    def __str__(self) -> str:
        return str(self.name)

    def __repr__(self) -> str:
        return f"Ingredient(pk={repr(self.pk)}, title={repr(self.name)})"

    class Meta:
        ordering = ("name",)
