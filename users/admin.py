from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.utils.safestring import mark_safe
from django.urls import reverse
from common.admin import Play2LearnAdmin
from common.utils.admin import append_fields, move_fields, remove_fields

CustomUser = get_user_model()

@admin.register(CustomUser)
class CustomUserAdmin(Play2LearnAdmin, UserAdmin):
    model = CustomUser

    readonly_fields = ['password_form']

    list_display = UserAdmin.list_display + ('is_superuser',)
    list_display_links = ('username', 'email', 'first_name', 'last_name')
    list_filter = ('is_staff', 'is_active')
    search_fields = ('username', 'email')
    ordering = ('username',)

    personal_fields = ('dob', 'avatar')
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