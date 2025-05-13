from django.contrib import admin
from .models import MathFactsScore, AnagramHuntScore
@admin.register(MathFactsScore)
class MathFactsScoresAdmin(admin.ModelAdmin):
    model = MathFactsScore
    list_display = ['user', 'score', 'date']

    def get_readonly_fields(self, request, obj=None):
        if obj: 
            return ('user', 'score', 'date')
        return () 
@admin.register(AnagramHuntScore)
class AnagramHuntScoresAdmin(admin.ModelAdmin):
    model = AnagramHuntScore
    list_display = ['user', 'score', 'date']

    def get_readonly_fields(self, request, obj=None):
        if obj:  
            return ('user', 'score', 'date')
        return () 
