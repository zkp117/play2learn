from django.urls import path

from .views import ReviewsAnagramAppView, ReviewsMathAppView, ReviewsAppThanksView

app_name = 'reviews'
urlpatterns = [
    path('write_review/anagram/', ReviewsAnagramAppView.as_view(), name='write_review/anagram'),
    path('write_review/math/', ReviewsMathAppView.as_view(), name='write_review/math'),
    path('reviews/review_thanks/', ReviewsAppThanksView.as_view(), name='review_thanks'),
]