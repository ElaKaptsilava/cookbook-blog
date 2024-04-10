from django.contrib import admin

from recipes_manager.models import Recipe, Instruction, IngredientRecipe, Category


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    pass


@admin.register(IngredientRecipe)
class IngredientRecipeAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Instruction)
class InstructionAdmin(admin.ModelAdmin):
    pass
