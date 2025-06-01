from django import forms
from allauth.account.forms import SignupForm
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext_lazy as _
from django_password_eye.fields import PasswordEye
from datetime import datetime
from django.contrib.auth import get_user_model
from django.forms.widgets import ClearableFileInput

BIRTH_YEAR_CHOICES = range(1915, datetime.now().year)
class CustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=50, required=False)
    last_name = forms.CharField(max_length=50, required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Optional: remove confirm password field
        self.fields.pop('password2', None)

    def signup(self, request, user):
        user.first_name = self.cleaned_data.get('first_name', '')
        user.last_name = self.cleaned_data.get('last_name', '')
        user.save()
        return user
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
            

