from rest_framework import viewsets
from .models import *
# <<<<<<< HEAD
from .serializers import RatingSerializer, ReviewSerializer
# =======
from .serializers import RatingSerializer, ReviewSerializer, CommunityOpinionSerializer
# >>>>>>> 31ca11baf66af229b91bf75b6aa6bf35a2ac57ec


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer


class CommunityOpinionViewSet(viewsets.ModelViewSet):
    queryset = CommunityOpinion.objects.all()
    serializer_class = CommunityOpinionSerializer
