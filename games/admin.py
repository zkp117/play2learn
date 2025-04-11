from django.contrib import admin
from .models import MathFactsScore, AnagramHuntScore

# MathFacts Scores Admin
@admin.register(MathFactsScore)
class MathFactsScoresAdmin(admin.ModelAdmin):
    model = MathFactsScore
    list_display = ['user', 'score', 'created_at']

    # Prevent editing of fields when editing an existing record
    def get_readonly_fields(self, request, obj=None):
        if obj:  # If it's an existing object, make the fields read-only
            return ('user', 'score', 'created_at')
        return ()  # Fields are editable when creating new records

# AnagramHunt Scores Admin
@admin.register(AnagramHuntScore)
class AnagramHuntScoresAdmin(admin.ModelAdmin):
    model = AnagramHuntScore
    list_display = ['user', 'score', 'created_at']

    # Prevent editing of fields when editing an existing record
    def get_readonly_fields(self, request, obj=None):
        if obj:  # If it's an existing object, make the fields read-only
            return ('user', 'score', 'created_at')
        return ()  # Fields are editable when creating new records
