# play2learn/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),

    # Add vue-games prefix to game URLs
    path("vue-games/anagram-hunt/", include('games.urls', namespace='games')),  # Anagram Hunt game
    path("vue-games/math-facts/", include('games.urls', namespace='games')),  # Math Facts game

    # Other paths
    path("accounts/", include("allauth.urls")),
    path('', include('pages.urls')),
    path('', include('users.urls')),
    path('', include('reviews.urls')),
    path('scoreboards/', include('scoreboards.urls')),
]
