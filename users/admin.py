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

    readonly_fields = ['password_form', 'get_anagramhunt_scores', 'get_mathfacts_scores', 'avatar_display', 'get_math_reviews', 'get_anagram_reviews']

    list_display = UserAdmin.list_display + ('is_superuser', 'get_anagramhunt_scores', 'get_mathfacts_scores','get_math_reviews', 'get_anagram_reviews')
    list_display_links = ('username', 'email', 'first_name', 'last_name')

    fieldsets = UserAdmin.fieldsets + (
        ('Game Scores', {'fields': ('get_anagramhunt_scores', 'get_mathfacts_scores')}),
        ('Game Reviews', {'fields': ('get_anagram_reviews', 'get_math_reviews')}),
        ('Personal Information', {'fields': ('dob', 'avatar')}), 
    )

    def password_form(self, obj):
        url = reverse('admin:auth_user_password_change', args=[obj.pk])
        return mark_safe(f'<a href="{url}">Change Password</a>')
    
    def avatar_display(self, obj):
        if obj.avatar:
            return mark_safe(f'<img src="{obj.avatar.url}" width="50" height="50"/>')
        return "No Avatar"
    avatar_display.short_description = 'Avatar'

    # setup display for AnagramHunt scores
    def get_anagramhunt_scores(self, obj):
        top_score = obj.math_scores.order_by('-score').first()
        return top_score.score if top_score else 0
    get_anagramhunt_scores.short_description = "Highest AnagramHunt Score"

    def get_mathfacts_scores(self, obj):
        top_score = obj.anagram_scores.order_by('-score').first()
        return top_score.score if top_score else 0
    get_mathfacts_scores.short_description = "Highest MathFacts Score"

    def get_math_reviews(self,obj):
        reviews = obj.math_reviews.all()
        collected_reviews = [review.review_text for review in reviews]
        return collected_reviews or None
    get_math_reviews.short_description = 'MathFacts Review(s)'
    
    def get_anagram_reviews(self, obj):
        reviews = obj.anagram_reviews.all()
        collected_reviews = [review.review_text for review in reviews]
        return collected_reviews or None
    get_anagram_reviews.short_description = 'AnagramHunts Review(s)'

