app_name = 'games'

from django.urls import path
from .views import (MathFactsView, 
                    AnagramHuntView, 
                    EnterMathFactsScore, 
                    EnterAnagramHuntScore,
                    is_logged_in)

urlpatterns = [
    path('math-facts/', MathFactsView.as_view(), name='math-facts'),
    path('anagram-hunt/', AnagramHuntView.as_view(), name='anagram-hunt'),
    path("api/record-score/mathfacts/", EnterMathFactsScore.as_view(), name="record_mathfacts_score"),
