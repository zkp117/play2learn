from django.urls import path
from .views import ReviewsAnagramAppView, ReviewsMathAppView, ReviewsAppThanksView

app_name = 'reviews'
urlpatterns = [
    path('write-anagram/', ReviewsAnagramAppView.as_view(), name='write_review_anagram'),
    path('write-math/', ReviewsMathAppView.as_view(), name='write_review_math'),  # Corrected the path and name
    path('reviews/review_thanks/', ReviewsAppThanksView.as_view(), name='review_thanks'),
]
