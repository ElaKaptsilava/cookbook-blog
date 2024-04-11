from django.contrib import admin

from reviews_ratings.models import Review, Rating, CommunityOpinion


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    pass


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    pass


@admin.register(CommunityOpinion)
class CommunityOpinionAdmin(admin.ModelAdmin):
    pass
