from django.urls import path

from .views import AboutUsView, HomePageView, AnagramHuntView, MathFactsView, CustomLoginView, MyPlay2LearnView

app_name = 'pages'
urlpatterns = [
    path('templates/', CustomLoginView.as_view(), name='login'),
    path('', HomePageView.as_view(), name='homepage'),
    path('about-us/', AboutUsView.as_view(), name='about-us'),
    path('anagram-hunt/', AnagramHuntView.as_view(), name='anagram-hunt'),
    path('my-play2learn/', MyPlay2LearnView.as_view(), name='my-play2learn'),
    path('math-facts/', MathFactsView.as_view(), name='math-facts')
]