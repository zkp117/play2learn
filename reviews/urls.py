from django.urls import path
from .views import ReviewsAnagramAppView, ReviewsMathAppView, ReviewsAppThanksView

app_name = 'vue-reviews'
urlpatterns = [
    path('reviewing_anagram/', ReviewsAnagramAppView.as_view(), name='reviewing_anagram'),
    path('reviewing_math/', ReviewsMathAppView.as_view(), name='reviewing_math'),
    path('review_thanks/', ReviewsAppThanksView.as_view(), name='review_thanks'),
]
