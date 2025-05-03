from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("accounts/", include("allauth.urls")),
    path("admin/", admin.site.urls),
    path('api/', include("games.urls")),
    path('',include("pages.urls")),
    path('', include('users.urls')),
    path('',include('reviews.urls')),
    path('scoreboards/',include('scoreboards.urls')),
]
