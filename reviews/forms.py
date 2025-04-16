from django import forms

GAME_CHOICES = {
    'Anagram Hunt',
    'Math Facts',
}

WORDLENGTH_REVIEW_CHOICES = {
    '5',
    '6',
    '7',
    '8',
}

MATHLEVEL_REVIEW_CHOICES = {
    [1-100]
}


class ReviewsForm(forms.Form):
    email = forms.EmailField()
    game_choices = [...]
    prerequsent = [...]
    user_review = [...]
    review_viewability = [...]


