from rest_framework import serializers
from .models import Recipe, Category, IngredientRecipe, Instruction


class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class IngredientRecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = IngredientRecipe
        fields = "__all__"


class InstructionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instruction
        fields = "__all__"
