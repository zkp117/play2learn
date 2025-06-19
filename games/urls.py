from django.urls import path, re_path
from django.views.generic import TemplateView
from .views import (
    EnterMathFactsScore,
    EnterAnagramHuntScore,
    is_logged_in,
)

app_name = 'games'
urlpatterns = [
    re_path(r'^anagram-hunt(?:/.*)?$', TemplateView.as_view(template_name='vue-templates/anagram-hunt.html'), name='vue-anagram-hunt'),
    re_path(r'^math-facts(?:/.*)?$', TemplateView.as_view(template_name='vue-templates/math-facts.html'), name='vue-math-facts'),

    # API endpoints
    path("api/record-score/mathfacts/", EnterMathFactsScore.as_view(), name="record_mathfacts_score"),
    path("api/record-score/anagramhunt/", EnterAnagramHuntScore.as_view(), name="record_anagramhunt_score"),
    path("api/is-logged-in/", is_logged_in, name="is_logged_in"),
]

