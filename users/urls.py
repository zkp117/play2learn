from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from . import views
from .views import MyAccountPageView, CustomLoginView, PasswordEmailView

from django.contrib.auth.views import (
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,

)

urlpatterns = [
    path("login/", CustomLoginView.as_view(), name="login"),
    
    # login & password reset with email
    path('account/password_reset/', PasswordResetView.as_view(template_name='account/password/password_reset.html'), name='password_reset'),
    path('account/password_reset_done/', PasswordResetDoneView.as_view(template_name='account/password/password_reset_done.html'), name='password_reset_done'),
    path( "account/reset/<uidb64>/<token>/", PasswordResetConfirmView.as_view(template_name='account/password/password_reset_confirm.html'), name="password_reset_confirm"),
    path( "account/reset/done/", PasswordResetCompleteView.as_view(template_name='account/password/password_reset_complete.html'), name="password_reset_complete"),

    # re-setting password through email
    path('account/password_reset/', PasswordEmailView.as_view(template_name='account/password/password_reset.html'), name='password_reset'),

    # user accounts
    path('my-account/', MyAccountPageView.as_view(), name='my-account'),
    path('clear-avatar/', views.clear_avatar, name='clear_avatar'), 
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
