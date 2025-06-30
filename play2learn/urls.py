from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from allauth.socialaccount.models import SocialToken, SocialAccount, SocialApp
from users.views import homepage_view

urlpatterns = [
    path('', include('users.urls')),
    path("accounts/", include("allauth.urls")),
    path("admin/", admin.site.urls),
    path('', homepage_view, name='home'),
    path('contact/', include('contact.urls', namespace='contact')),
    path('', include("pages.urls")),
    path('', include('reviews.urls')),
    path('scoreboards/', include('scoreboards.urls')),
    path('', include('games.urls', namespace='games')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# takes out these sections from admin
admin.site.unregister(SocialToken)
admin.site.unregister(SocialAccount)
admin.site.unregister(SocialApp)
