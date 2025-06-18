from django.urls import path
from django.views.generic import TemplateView
from .views import (
    RedirectMathFacts,
    RedirectAnagramHunt,
    EnterMathFactsScore,
    EnterAnagramHuntScore,
    is_logged_in,
)

app_name = 'games'

urlpatterns = [
    # These routes are meant to be accessed at /math-facts/ and /anagram-hunt/
    path('math-facts/', RedirectMathFacts.as_view(), name='math-facts'),
    path('anagram-hunt/', RedirectAnagramHunt.as_view(), name='anagram-hunt'),
    path('anagram-hunt/', TemplateView.as_view(template_name='vue-templates/anagram-hunt.html')),
    path('math-facts/', TemplateView.as_view(template_name='vue-templates/math-facts.html')),

    # These are API endpoints used by the Vue frontend
    path("api/record-score/mathfacts/", EnterMathFactsScore.as_view(), name="record_mathfacts_score"),
    path("api/record-score/anagramhunt/", EnterAnagramHuntScore.as_view(), name="record_anagramhunt_score"),
    path("api/is-logged-in/", is_logged_in, name="is_logged_in"),
]
