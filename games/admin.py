from django.contrib import admin
from .models import Scores
@admin.register(Scores)
class ScoresAdmin(admin.ModelAdmin):
    model = Scores
    list_display = ['scores', 'created', 'updated']

    def get_readonly_fields(self, request, obj=None):
        if obj: # editing an existing object
            return ('created', 'updated')

        return ()
