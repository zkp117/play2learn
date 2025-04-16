from django import forms

GAME_CHOICES = [
    ('1', 'Choose Game'),
    ('2', 'Math Facts'),
    ('3', 'Anagram Hunt'),
]

PREREQUISITE_QUESTION = [
    ('1', 'No (neither game)'),
    ('2', 'Yes (Anagram Hunt only)'),
    ('3', 'Yes (Math Facts only)'),
    ('4', 'Yes (Both games)'),
]

WORDLENGTH_REVIEW_CHOICES = [(i, str(i)) for i in range(5,8)]
MATHLEVEL_REVIEW_CHOICES = [(i, str(i)) for i in range(1, 101)]

class ReviewsForm(forms.Form):
    email = forms.EmailField(
        label="Your email address"
    )

    game = forms.ChoiceField(
        choices=GAME_CHOICES,
        label="Select A Game")
    
    prerequisite = forms.ChoiceField(
        choices=PREREQUISITE_QUESTION,
        label="Have you reviewed a game before?")
    
    user_review = forms.CharField(
        widget=forms.Textarea,
        label="Write you review here!")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        selected_game = self.data.get('game') or self.initial.get('game')

        if selected_game == '2':
            self.fields['math_level'] = forms.ChoiceField(
                chocies=MATHLEVEL_REVIEW_CHOICES,
                label="Which math level did you last play?",
                required=True
            )
        elif selected_game == '3':
            self.fields['anagram_level'] = forms.ChoiceField(
                choices=WORDLENGTH_REVIEW_CHOICES,
                label="Which word level did you last play?",
                required=True
            )