from rest_framework import serializers
from .models import *


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'


class CommunityOpinionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommunityOpinion
        fields = '__all__'
