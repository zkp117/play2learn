from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("accounts/", include("allauth.urls")),
    path("admin/", admin.site.urls),
    
    # Corrected include for 'games' app with the 'app_name' and 'namespace'
    path('games/', include(('games.urls', 'games'), namespace='games')),
    
    # Include other apps with clear paths
    path('', include("pages.urls")),
    path('', include('users.urls')),
    path('', include('reviews.urls')),
    path('scoreboards/', include('scoreboards.urls')),
]
