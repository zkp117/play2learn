from django.urls import path
from django.views.generic import TemplateView
from .views import (
    EnterMathFactsScore,
    EnterAnagramHuntScore,
    is_logged_in,
)

app_name = 'games'

urlpatterns = [

    # API endpoints
    path("api/record-score/mathfacts/", EnterMathFactsScore.as_view(), name="record_mathfacts_score"),
    path("api/record-score/anagramhunt/", EnterAnagramHuntScore.as_view(), name="record_anagramhunt_score"),
    path("api/is-logged-in/", is_logged_in, name="is_logged_in"),
]