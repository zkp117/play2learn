from django import forms
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm
from django.template.loader import render_to_string
from common.utils.email_service import send_email
from django.utils.translation import gettext_lazy as _
from django_password_eye.fields import PasswordEye
from datetime import datetime
from django.contrib.auth import get_user_model
from django.forms.widgets import ClearableFileInput

BIRTH_YEAR_CHOICES = range(1915, datetime.now().year)

class CustomUserChangeForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ('email', 'username', 'first_name', 'last_name', 'dob', 'avatar',
                 )
        widgets = {
            'dob': forms.SelectDateWidget(
                attrs={
                    'style': 'width: 31%; display: inline-block; margin: 0 1%'
                },
                years=BIRTH_YEAR_CHOICES
            ),
            'avatar': ClearableFileInput(attrs={'class': 'form-control-file'})
        }
class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Username')}),
        label='Username'
    )
    password = PasswordEye(
        label='Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': _('Password')})
    )

    # helps clean to load smoother / faster
    def clean(self):
        return super().clean()
            

