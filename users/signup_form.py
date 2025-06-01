from django import forms
from allauth.account.forms import SignupForm
class CustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=50, required=False)
    last_name = forms.CharField(max_length=50, required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Remove password2 field
        if 'password2' in self.fields:
            del self.fields['password2']

    def clean(self):
        # Remove password2 validation
        cleaned_data = super().clean()
        return cleaned_data

    def signup(self, request, user):
        user.first_name = self.cleaned_data.get('first_name', '')
        user.last_name = self.cleaned_data.get('last_name', '')
        user.save()
        return user
