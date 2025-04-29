from django import forms

PREREQUISITE_QUESTION = [
    ('1', 'No'),
    ('2', 'Yes'),
]
class ReviewsMathForm(forms.Form):
    email = forms.EmailField(
        label="Your email address"
    )
    
    prerequisite = forms.ChoiceField(
        choices=PREREQUISITE_QUESTION,
        label="Have you reviewed this game before?")
    
    user_review = forms.CharField(
        widget=forms.Textarea,
        label="Write you review here!")

class ReviewsAnagramForm(forms.Form):

    transfered_score = [...]  # the score from the game just completed

    email = forms.EmailField(
        label="Your email address"
    )
    
    prerequisite = forms.ChoiceField(
        choices=PREREQUISITE_QUESTION,
        label="Have you reviewed this game before?")
    
    user_review = forms.CharField(
        widget=forms.Textarea,
        label="Write you review here!")