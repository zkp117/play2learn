from django.urls import path
from django.views.generic import TemplateView
from .views import (AboutUsView, 
                    HomePageView, 
                    CustomLoginView, 
                    MyScoresView)

app_name = 'pages'
urlpatterns = [
    path('templates/', CustomLoginView.as_view(), name='login'),
    path('', HomePageView.as_view(), name='homepage'),
    path('about-us/', AboutUsView.as_view(), name='about-us'),
    path('my-scores/', MyScoresView.as_view(), name='my-scores'),
    path('vue-games/math-facts/', TemplateView.as_view(template_name='vue-templates/math-facts.html'), name='vue-math-facts'),
    path('vue-games/anagram-hunt/', TemplateView.as_view(template_name='vue-templates/anagram-hunt.html'), name='vue-anagram-hunt'),
]