from django.urls import path
from .views import ScoreBoards

app_name = 'scoreboards'

urlpatterns = [
    path('',ScoreBoards.as_view(), name='scoreboards')

]