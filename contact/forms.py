from django import forms

class ContactStaffForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    message = forms.CharField(
        label = 'Write your question or comment here!',
        widget=forms.Textarea
    )