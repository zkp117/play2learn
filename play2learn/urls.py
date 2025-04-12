from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("accounts/", include("allauth.urls")),
    path("admin/", admin.site.urls),
    path('', include("games.urls")),
    path('',include("pages.urls")),
    path('', include('users.urls')),
]
