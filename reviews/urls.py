from django.urls import path

from .views import ReviewsAppView, ReviewsAppThanksView

app_name = 'reviews'
urlpatterns = [
    path('reviews/write_review/', ReviewsAppView.as_view(), name='write_review'),
    path('reviews/review_thanks/', ReviewsAppThanksView.as_view(), name='review_thanks'),
]