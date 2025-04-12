from django.urls import path

from .views import AboutUsView, HomePageView, AnagramHuntView, MathFactsView

app_name = 'pages'
urlpatterns = [
    path('', HomePageView.as_view(), name='homepage'),
    path('about-us/', AboutUsView.as_view(), name='about-us'),
    path('anagram-hunt/', AnagramHuntView.as_view(), name='anagram-hunt'),
    path('math-facts/', MathFactsView.as_view(), name='math-facts')
]