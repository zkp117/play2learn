from django.contrib import admin
from .models import MathFactsScoreBoard, AnagramHuntScoreBoard

# MathFacts ScoreBoard Admin
@admin.register(MathFactsScoreBoard)
class MathFactsScoreBoardAdmin(admin.ModelAdmin):
    model = MathFactsScoreBoard
    list_display = ['score', 'user', 'date_added']  # Add your fields
    # Customize other settings here

# AnagramHunt ScoreBoard Admin
@admin.register(AnagramHuntScoreBoard)
class AnagramHuntScoreBoardAdmin(admin.ModelAdmin):
    model = AnagramHuntScoreBoard
    list_display = ['score', 'user', 'date_added']  # Add your fields
    # Customize other settings here
