from django import forms
from users.models import CustomUser
class ReviewsMathForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['math_reviews']
        labels = {
            'math_reviews': 'Write your review here!',
        }
        widgets = {
            'math_reviews': forms.Textarea(
                attrs={'placeholder': 'If you want, you can say what number level you chose and what your score was.'}),
        }
class ReviewsAnagramForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['anagram_reviews']
        labels = {
            'anagram_reviews': 'Write your review here!',
        }
        widgets = {
            'anagram_reviews': forms.Textarea(
                attrs={'placeholder': 'If you want, you can say which word letter length you chose and what your score was.'}),
        }