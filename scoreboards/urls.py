from django.urls import path
from .views import ScoreBoards, UserScores

app_name = 'scoreboards'

urlpatterns = [
    path('',ScoreBoards.as_view(), name='scoreboards'),
    path('my-scores/',UserScores.as_view(), name='my-scores')
]