from django.urls import path
from django.conf.urls.static import static

from .views import DjangoPasswordChangeView, MyAccountPageView

from django.conf import settings

from . import views

urlpatterns = [
    path("password/change/", DjangoPasswordChangeView.as_view(), name="account_change_password"),  # Updated view name
    path('my-account/', MyAccountPageView.as_view(), name='my-account'),
    path('clear-avatar/', views.clear_avatar, name='clear_avatar'), 
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)