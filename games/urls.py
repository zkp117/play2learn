from django.urls import path
from . import views

urlpatterns = [
    # Path for games page (root of the Vue app)
    path('', views.game_view, name='games-home'),  # Serve the Vue app on /games/

    # Game-specific URLs (may not be needed since Vue Router handles the routing)
    path('math-facts/', views.game_view, name='math-facts'),
    path('anagram-hunt/', views.game_view, name='anagram-hunt'),

    # API endpoints
    path("api/record-score/mathfacts/", EnterMathFactsScore.as_view(), name="record_mathfacts_score"),
]
