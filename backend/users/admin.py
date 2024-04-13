from django.contrib import admin
from .models import CustomUser, ChefProfile


@admin.register(CustomUser)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(ChefProfile)
class ChefProfileAdmin(admin.ModelAdmin):
    pass