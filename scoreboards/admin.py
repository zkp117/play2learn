from django.contrib import admin
from .models import ( MathFactsScoreBoard, 
                     AnagramHuntScoreBoard,
                     MathFactsUserScores,
                     AnagramHuntUserScores)

@admin.register(MathFactsScoreBoard)
class MathFactsScoreBoardAdmin(admin.ModelAdmin):
    model = MathFactsScoreBoard
    list_display = ['score', 'user', 'date_added']
@admin.register(AnagramHuntScoreBoard)
class AnagramHuntScoreBoardAdmin(admin.ModelAdmin):
    model = AnagramHuntScoreBoard
    list_display = ['score', 'user', 'date_added']

@admin.register(MathFactsUserScores)
class MathFactsUserScoresAdmin(admin.ModelAdmin):
    list_display = ['user', 'score', 'operation', 'max_number', 'seconds_left', 'date_added']

@admin.register(AnagramHuntUserScores)
class AnagramHuntUserScoresAdmin(admin.ModelAdmin):
    list_display = ['user', 'score', 'word_length', 'seconds_left', 'date_added']