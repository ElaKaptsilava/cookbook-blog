from django.contrib import admin

from reviews_ratings.models import Review, Rating


# Register your models here.

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    pass


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    pass
