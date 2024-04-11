from rest_framework import viewsets

from .models import Recipe, Category, IngredientRecipe, Instruction
from .serializers import (
    RecipeSerializer,
    CategorySerializer,
    IngredientRecipeSerializer,
    InstructionSerializer
)


class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class IngredientRecipeViewSet(viewsets.ModelViewSet):
    queryset = IngredientRecipe.objects.all()
    serializer_class = IngredientRecipeSerializer


class InstructionViewSet(viewsets.ModelViewSet):
    queryset = Instruction.objects.all()
    serializer_class = InstructionSerializer
