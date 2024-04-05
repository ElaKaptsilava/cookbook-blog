from rest_framework.routers import DefaultRouter

from .views import IngredientViewSet, InitialIngredientViewSet

app_name = "nutrition"

router = DefaultRouter()

router.register(r"ingredients", IngredientViewSet, basename="ingredients")
router.register(r'initial-ingredients', InitialIngredientViewSet, basename="initial-ingredients")
