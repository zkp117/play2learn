from django.urls import path
from .views import ReviewsAnagramAppView, ReviewsMathAppView, ReviewsAppThanksView

app_name = 'reviews'
urlpatterns = [
    path('write_review_anagram/', ReviewsAnagramAppView.as_view(), name='write_review_anagram'),
    path('write_review_math/', ReviewsMathAppView.as_view(), name='write_review_math'),
    path('review_thanks/', ReviewsAppThanksView.as_view(), name='review_thanks'),
]
