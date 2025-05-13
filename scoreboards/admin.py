from django.contrib import admin
from .models import MathFactsScoreBoard, AnagramHuntScoreBoard
@admin.register(MathFactsScoreBoard)
class MathFactsScoreBoardAdmin(admin.ModelAdmin):
    model = MathFactsScoreBoard
    list_display = ['score', 'user', 'date_added']
@admin.register(AnagramHuntScoreBoard)
class AnagramHuntScoreBoardAdmin(admin.ModelAdmin):
    model = AnagramHuntScoreBoard
    list_display = ['score', 'user', 'date_added']
