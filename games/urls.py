from django.urls import path
from .views import MathFactsView, AnagramHuntView, EnterMathFactsScore

urlpatterns = [
    path('math-facts/', MathFactsView.as_view(), name='math-facts'),
    path('anagram-hunt/', AnagramHuntView.as_view(), name='anagram-hunt'),

    
    path("api/record-score/mathfacts/", EnterMathFactsScore.as_view(), name="enter_mathfacts_score"),
]