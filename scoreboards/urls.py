from django.urls import path
from .views import ScoreBoards

app_name = 'templates'
urlpatterns = [
    path('scoreboards/',ScoreBoards.as_view(), name='scoreboards')

]