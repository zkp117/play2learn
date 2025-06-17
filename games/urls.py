app_name = 'games'

from django.urls import path
from .views import (
    RedirectMathFacts,
    RedirectAnagramHunt,
    EnterMathFactsScore,
    EnterAnagramHuntScore,
    is_logged_in,
)

urlpatterns = [
    path('math-facts/', RedirectMathFacts.as_view(), name='math-facts'),
    path('anagram-hunt/', RedirectAnagramHunt.as_view(), name='anagram-hunt'),
    path("api/record-score/mathfacts/", EnterMathFactsScore.as_view(), name="record_mathfacts_score"),
    path("api/record-score/anagramhunt/", EnterAnagramHuntScore.as_view(), name="record_anagramhunt_score"),
    path("api/is-logged-in/", is_logged_in, name="is_logged_in"),
]
