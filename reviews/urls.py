from django.urls import path

from .views import ReviewsAnagramAppView, ReviewsMathAppView, ReviewsAppThanksView

app_name = 'reviews'
urlpatterns = [
    path('write/', ReviewsAnagramAppView.as_view(), name='write_review/anagram'),
    path('write/', ReviewsMathAppView.as_view(), name='write_review_math'),
    path('reviews/review_thanks/', ReviewsAppThanksView.as_view(), name='review_thanks'),
]