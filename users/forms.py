from django import forms
from django_password_eye.fields import PasswordEye
from datetime import datetime
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model

BIRTH_YEAR_CHOICES = range(1915, datetime.now().year)
class CustomUserChangeForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['email', 'username', 'first_name', 'last_name', 'dob', 'avatar'] 
        widgets = {
            'dob': forms.SelectDateWidget(
                attrs={'style': 'width: 31%; display: inline-block; margin: 0 1%'},
                years=BIRTH_YEAR_CHOICES
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'avatar' in self.fields:
            self.fields['avatar'].widget.attrs.update({'class': 'form-control'})

# this is part of the password eye
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
    def clean(self):
        return super().clean()