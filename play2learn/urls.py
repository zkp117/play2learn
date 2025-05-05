from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("accounts/", include("allauth.urls")),
    path("admin/", admin.site.urls),
    path('games/', include(('games.urls', 'games'), namespace='games')),
    path('',include("pages.urls")),
    path('', include('users.urls')),
    path('',include('reviews.urls')),
    path('scoreboards/',include('scoreboards.urls')),
]
