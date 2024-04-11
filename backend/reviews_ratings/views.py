from rest_framework import viewsets
from .models import *
from .serializers import RatingSerializer, ReviewSerializer, CommunityOpinionSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer


class CommunityOpinionViewSet(viewsets.ModelViewSet):
    queryset = CommunityOpinion.objects.all()
    serializer_class = CommunityOpinionSerializer
