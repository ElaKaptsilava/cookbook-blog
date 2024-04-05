from rest_framework import serializers
from rest_framework.exceptions import APIException

from .models import Ingredient


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = "__all__"


class InitialIngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ["name"]

    def validate(self, attrs):
        ingredient = Ingredient.objects.filter(name=attrs.get("name"))
        if ingredient.exists():
            raise APIException("Ingredient already exists")
        return attrs
