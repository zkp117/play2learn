from . import views
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import MyAccountPageView, CustomLoginView, PasswordEmailView, CustomSignupView
from django.contrib.auth.views import (
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView
)

urlpatterns = [
    path("login/", CustomLoginView.as_view(), name="login"),

    # Password reset workflow
    path('account/password_reset/', PasswordEmailView.as_view(template_name='account/password/password_reset.html'), name='password_reset'),
    path('account/password_reset_done/', PasswordResetDoneView.as_view(template_name='account/password/password_reset_done.html'), name='password_reset_done'),
    path('account/reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='account/password/password_reset_confirm.html'), name='password_reset_confirm'),
    path('account/reset/done/', PasswordResetCompleteView.as_view(template_name='account/password/password_reset_complete.html'), name='password_reset_complete'),
    path('signup/', CustomSignupView.as_view(), name='account_signup'),

    # User account
    path('my-account/', MyAccountPageView.as_view(), name='my-account'),
    path('clear-avatar/', views.clear_avatar, name='clear_avatar'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
