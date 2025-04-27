from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("accounts/", include("allauth.urls")),
    path("admin/", admin.site.urls),
    path("games/", include("games.urls")),
    path("pages/", include("pages.urls")),
    path("users/", include("users.urls")),
    path('reviews/', include('reviews.urls')),
]

