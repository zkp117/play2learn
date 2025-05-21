from django.urls import path

from .views import AboutUsView, HomePageView, ContactUsView, AnagramHuntView, MathFactsView, CustomLoginView, MyScoresView

app_name = 'pages'
urlpatterns = [
    path('templates/', CustomLoginView.as_view(), name='login'),
    path('', HomePageView.as_view(), name='homepage'),
    path('about-us/', AboutUsView.as_view(), name='about-us'),
    path('contact-us/', ContactUsView.as_view(), name="contact-us"),
    path('anagram-hunt/', AnagramHuntView.as_view(), name='anagram-hunt'),
    path('my-scores/', MyScoresView.as_view(), name='my-scores'),
    path('math-facts/', MathFactsView.as_view(), name='math-facts'),
]