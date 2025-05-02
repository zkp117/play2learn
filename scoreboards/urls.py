from django.urls import path
from .views import ScoreBoards

app_name = 'vue-scoreboards'

urlpatterns = [
    path('scoreboards/',ScoreBoards.as_view(), name='scoreboards')

]