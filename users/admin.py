from django.contrib import admin
from django.contrib.auth import get_user_model
from django.utils.safestring import mark_safe
from django.urls import reverse
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from reviews.models import GameReviews

CustomUser = get_user_model()
@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):

    model = CustomUser
    
    readonly_fields = ['password_form', 'get_anagramhunt_scores', 
                       'get_mathfacts_scores', 'avatar_display', 
                       'get_math_reviews', 'get_anagram_reviews']

    list_display = UserAdmin.list_display + ('is_superuser', 'get_anagramhunt_scores', 
                                             'get_mathfacts_scores','get_math_reviews', 
                                             'get_anagram_reviews')
    list_display_links = ('username', 'email', 'first_name', 'last_name')

    fieldsets = UserAdmin.fieldsets + (
        ('Game Scores', {'fields': ('get_anagramhunt_scores', 'get_mathfacts_scores')}),
        ('Game Reviews', {'fields': ('get_math_reviews', 'get_anagram_reviews')}),
        ('Personal Information', {'fields': ('dob', 'avatar')}), 
        )

    def password_form(self, obj):
        url = reverse('admin:auth_user_password_change', args=[obj.pk])
        return mark_safe(f'<a href="{url}">Change Password</a>')
    
    def avatar_display(self, obj):
        if obj.avatar:
            try:
                return mark_safe(f'<img src="{obj.avatar.url}" width="50" height="50"/>')
            except Exception as e:
                return f"Error loading avatar: {e}"
        return "No Avatar"

    # setup display for AnagramHunt scores
    def get_anagramhunt_scores(self, obj):
        top_score = obj.anagram_scores.order_by('-score').first()
        return top_score.score if top_score else 0
    get_anagramhunt_scores.short_description = "Highest AnagramHunt Score"

    # setup display for MathFacts scores
    def get_mathfacts_scores(self, obj):
        top_score = obj.math_scores.order_by('-score').first()
        return top_score.score if top_score else 0
    get_mathfacts_scores.short_description = "Highest MathFacts Score"

    # setup display for MathFacts reviews
    def get_math_reviews(self, obj):
        review = GameReviews.objects.filter(user = obj, game='mathfacts').order_by('-submitted').first()
        return review.review if review else "No review submitted"
    get_math_reviews.short_description = 'MathFacts Reviews'

    # setup display for AnagramHunt reviews
    def get_anagram_reviews(self, obj):
        review = GameReviews.objects.filter(user = obj, game='anagramhunt').order_by('-submitted').first()
        return review.review if review else 'No review submitted'
    get_anagram_reviews.short_description = 'AnagramHunt Reviews'