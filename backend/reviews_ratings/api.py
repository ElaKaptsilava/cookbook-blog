from rest_framework.routers import DefaultRouter
from .views import RatingViewSet, ReviewViewSet, CommunityOpinionViewSet

app_name = 'reviews_ratings'

router = DefaultRouter()
router.register(r'reviews', ReviewViewSet)
router.register(r'ratings', RatingViewSet)
router.register(r'community-opinion', CommunityOpinionViewSet)
