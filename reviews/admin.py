from django.contrib import admin
from .models import GameReviews

@admin.register(GameReviews)
class GameReviewsAdmin(admin.ModelAdmin):
    list_display = ('user', 'game', 'review', 'submitted')
    list_filter = ('game', 'submitted')
    search_fields = ('user__username', 'review')