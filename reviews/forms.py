from django import forms

GAME_CHOICES = {
    'Anagram Hunt',
    'Math Facts',
}

WORDLENGTH_REVIEW_CHOICES = [(i, str(i)) for i in range(5,8)]

MATHLEVEL_REVIEW_CHOICES = [(i, str(i)) for i in range(1, 101)]


class ReviewsForm(forms.Form):
    email = forms.EmailField()
    game_choices = [...]
    prerequsent = [...]
    user_review = [...]
    review_viewability = [...]

    if game_choices == 'Math Facts':
        math_level = forms.ChoiceField(choices=MATHLEVEL_REVIEW_CHOICES)

    if game_choices == 'Anagram Hunt':
        anagram_level = forms.ChoiceField(choices=WORDLENGTH_REVIEW_CHOICES)


