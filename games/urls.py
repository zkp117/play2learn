from django.urls import path
from .views import (
    AnagramHuntView,
    MathFactsView,
    EnterMathFactsScore,
    EnterAnagramHuntScore,
    is_logged_in,
)

app_name = 'games'

urlpatterns = [
    path('vue-games/math-facts/', MathFactsView.as_view(), name='vue-math-facts'),
    path('vue-games/anagram-hunt/', AnagramHuntView.as_view(), name='vue-anagram-hunt'),

    # API endpoints
    path("api/record-score/mathfacts/", EnterMathFactsScore.as_view(), name="record_mathfacts_score"),
    path("api/record-score/anagramhunt/", EnterAnagramHuntScore.as_view(), name="record_anagramhunt_score"),
    path("api/is-logged-in/", is_logged_in, name="is_logged_in"),
]