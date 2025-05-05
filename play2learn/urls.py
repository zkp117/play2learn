from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("accounts/", include("allauth.urls")),
    path("admin/", admin.site.urls),

    # Ensure this path includes Vue app routes
    path('games/', include(('games.urls'), namespace='games')),
    path('vue-games/', include('games_vue.urls', namespace='vue-games')),

    # Include other apps with their respective paths
    path('', include("pages.urls")),
    path('', include('users.urls')),
    path('', include('reviews.urls')),
    path('scoreboards/', include('scoreboards.urls')),
]
