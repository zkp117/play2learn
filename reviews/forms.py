from django import forms

GAME_CHOICES = {
    'Anagram Hunt',
    'Math Facts',
}
class ReviewsForm(forms.Form):
    email = forms.EmailField()
    game_choices = [...]
    user_review = [...]
    review_viewability = [...]


