from django.urls import path
from django.conf.urls.static import static
from . import views
from django.contrib.auth.views import PasswordResetView
from .views import MyAccountPageView, CustomLoginView
from django.conf import settings


urlpatterns = [
    path("login/", CustomLoginView.as_view(), name="login"),
    path('account/password_reset/', PasswordResetView.as_view(template_name='account/password/password_reset.html'), name='password_reset'),
    path('my-account/', MyAccountPageView.as_view(), name='my-account'),
    path('clear-avatar/', views.clear_avatar, name='clear_avatar'), 
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)