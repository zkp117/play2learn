from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.utils.safestring import mark_safe
from django.urls import reverse
from common.admin import Play2LearnAdmin
from .models import CustomUser
from common.utils.admin import append_fields, move_fields, remove_fields

CustomUser = get_user_model()
@admin.register(CustomUser)
class CustomUserAdmin(Play2LearnAdmin, UserAdmin):
    model = CustomUser

    readonly_fields = ['password_form']

    list_display = UserAdmin.list_display + ('is_superuser', 'get_anagramhunt_scores', 'get_mathfacts_scores',)
    list_display_links = ('username', 'email', 'first_name', 'last_name', 'get_anagramhunt_scores', 'get_mathfacts_scores')
    list_filter = ('is_staff', 'is_active')
    search_fields = ('username', 'email')
    ordering = ('username',)

    personal_fields = ('dob', 'avatar',)
    append_fields(UserAdmin.fieldsets, 'Personal info', personal_fields)

    move_fields(UserAdmin.fieldsets, 'Personal info', None, ('email',))

    remove_fields(UserAdmin.fieldsets, None, ('password',))

    append_fields(UserAdmin.fieldsets, None, ('password_form',))

    new_user_fields = ('email', )
    add_fieldsets = append_fields(UserAdmin.add_fieldsets, None, new_user_fields)

    optional_fields = ('first_name', 'last_name', 'dob')
    add_fieldsets = append_fields(UserAdmin.add_fieldsets, 'Optional Fields', optional_fields)

    def password_form(self, obj):
        url = reverse('admin:auth_user_password_change', args=[obj.pk])
        return mark_safe(f'<a href="{url}">Change Password</a>')

    def get_form(self, request, obj=None, **kwargs):
        self.save_on_top = obj is not None
        return super().get_form(request, obj, **kwargs)
    
    def get_anagramhunt_scores(self, obj):
    # Ensure the related_name is correct
        scores = obj.anagram_scores.all()  # This is accessing the related scores correctly
        total_score = sum(score.score for score in scores)  # Calculate total score
        return total_score
    
    def get_mathfacts_scores(self, obj):
        return obj.scores.filter(game='MathFacts').values_list('score', flat=True)

    get_mathfacts_scores.short_description = 'MathFacts Scores'


