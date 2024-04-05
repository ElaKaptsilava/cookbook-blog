from django.db import transaction
from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import Ingredient
from .serializers import IngredientSerializer, InitialIngredientSerializer
from .calorie_ninjas import CalorieNinjas


class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer


class InitialIngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = InitialIngredientSerializer

    @transaction.atomic
    def create(self, request, *args, **kwargs):
        serializer_initial_ingredients = self.serializer_class(data=request.data)
        serializer_initial_ingredients.is_valid(raise_exception=True)
        title = serializer_initial_ingredients.validated_data.get('name', None)
        ingredient_data = CalorieNinjas.get_nutrition_facts(title)[0]
        serializer_ingredient = IngredientSerializer(data=ingredient_data)
        serializer_ingredient.is_valid(raise_exception=True)
        serializer_ingredient.save()
        return Response(serializer_ingredient.data, status=status.HTTP_201_CREATED)
