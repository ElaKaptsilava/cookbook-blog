from django.db import models

from nutrition.models import Ingredient
from users.models import CustomUser


def user_directory_path(instance, filename: str) -> str:
    return f"user_{instance.email}/recipes/{filename}"


class Category(models.Model):
    title = models.CharField(max_length=256, help_text="Title of the category.")

    def __str__(self) -> str:
        return str(self.title)

    def __repr__(self) -> str:
        return f"Category(pk={repr(self.pk)}, title={repr(self.title)})"

    class Meta:
        ordering = ("title",)


class Recipe(models.Model):
    custom_user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        help_text="The user who created this recipe."
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        help_text="The category to which this recipe belongs."
    )
    cooking_time = models.IntegerField(
        default=0,
        help_text="The time it takes to cook this recipe (in minutes)."
    )
    title = models.CharField(
        max_length=256,
        help_text="The title of the recipe."
    )
    image = models.ImageField(
        upload_to=user_directory_path,
        blank=True,
        null=True,
        help_text="An image representing the recipe (optional)."
    )
    file = models.FileField(
        upload_to=user_directory_path,
        blank=True,
        null=True,
        help_text="A file containing the recipe instructions (optional)."
    )
    description = models.TextField(
        help_text="A description of the recipe."
    )
    ingredients = models.ManyToManyField(
        Ingredient,
        through="IngredientRecipe",
        help_text="The ingredients required for this recipe."
    )
    published_date = models.DateTimeField(
        auto_now_add=True,
        help_text="The date and time when this recipe was published."
    )

    def __str__(self) -> str:
        return str(self.title)

    def __repr__(self) -> str:
        return f"Recipe(pk={repr(self.pk)}, title={repr(self.title)}), user={repr(self.custom_user)})"

    class Meta:
        ordering = ("title",)


class IngredientRecipe(models.Model):
    class MeasuringUnit(models.TextChoices):
        milligram = "mg", "Milligram"
        gram = "g", "Gram"
        kg = "kg", "Kilogram"
        milliliter = "ml", "Milliliter"
        liter = "l", "Liter"

    title = models.CharField(
        max_length=256,
        default='Ingredient',
        help_text="Title of the ingredient in this recipe (optional)."
    )
    quantity = models.FloatField(
        help_text="Quantity of the ingredient needed for the recipe."
    )
    measuring_unit = models.CharField(
        max_length=256,
        choices=MeasuringUnit.choices,
        default=MeasuringUnit.gram,
        help_text="Unit of measurement for the quantity."
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        help_text="The recipe to which this ingredient belongs."
    )
    ingredient = models.OneToOneField(
        Ingredient,
        on_delete=models.CASCADE,
        help_text="The ingredient used in this recipe."
    )

    def __str__(self) -> str:
        return str(self.title)

    def __repr__(self) -> str:
        return f"IngredientRecipe(pk={repr(self.pk)}, title={repr(self.title)}, quantity={repr(self.quantity)})"


class Instruction(models.Model):
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        help_text="The recipe to which this instruction belongs."
    )
    number = models.IntegerField(
        help_text="The order or sequence number of this instruction within the recipe."
    )
    description = models.TextField(
        help_text="The detailed description of this instruction."
    )
    file = models.FileField(
        upload_to=user_directory_path,
        blank=True,
        null=True,
        help_text="An optional file containing additional information for this instruction."
    )

    def __str__(self) -> str:
        return f'{self.description[:20]}...'

    def __repr__(self) -> str:
        return f"Instruction(pk={repr(self.pk)}, recipe={repr(self.recipe)}, description={repr(f'{self.description[:20]}...')})"
