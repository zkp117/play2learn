from django import forms
from users.models import CustomUser
class ReviewsMathForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['mathfacts_reviews']
        labels = {
            'mathfacts_reviews': 'Write your review here!',
        }
        widgets = {
            'mathfacts_reviews': forms.Textarea(
                attrs={'placeholder': 'If you want, you can say what number level you chose and what your score was.'}),
        }
class ReviewsAnagramForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['anagramhunt_reviews']
        labels = {
            'anagramhunt_reviews': 'Write your review here!',
        }
        widgets = {
            'anagramhunt_reviews': forms.Textarea(
                attrs={'placeholder': 'If you want, you can say which word letter length you chose and what your score was.'}),
        }