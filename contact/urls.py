from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import ContactAppView, ContactAppThanksView

app_name = 'contact'
urlpatterns = [
    path('contact-us/', ContactAppView.as_view(), name='contact_form'),
    path('contact-thanks/', ContactAppThanksView.as_view(), name='thanks'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)