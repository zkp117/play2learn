from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.utils.safestring import mark_safe
from django.urls import reverse
from .models import CustomUser

CustomUser = get_user_model()
@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser

    readonly_fields = ['password_form', 'get_anagramhunt_scores', 'get_mathfacts_scores']

    list_display = UserAdmin.list_display + ('is_superuser', 'get_anagramhunt_scores', 'get_mathfacts_scores',)
    list_display_links = ('username', 'email', 'first_name', 'last_name')

    fieldsets = UserAdmin.fieldsets + (
        ('Game Scores', {'fields': ('get_anagramhunt_scores', 'get_mathfacts_scores')}),
    )

    def password_form(self, obj):
        url = reverse('admin:auth_user_password_change', args=[obj.pk])
        return mark_safe(f'<a href="{url}">Change Password</a>')

    def get_anagramhunt_scores(self, obj):
        scores = obj.anagram_scores.all()
        total_score = sum(score.score for score in scores)
        return total_score or 0

    get_anagramhunt_scores.short_description = 'Anagram Hunt Total Score'

    def get_mathfacts_scores(self, obj):
        scores = obj.math_scores.all()
        total_score = sum(score.score for score in scores)
        return total_score or 0

    get_mathfacts_scores.short_description = 'Math Facts Total Score'
