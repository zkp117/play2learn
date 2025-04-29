from django.urls import path
from .views import AllUsersAnagramScores, AllUsersMathScores, ScoreBoardsSummary

app_name = 'vue-scoreboards'
urlpatterns = [
    path('scoreboard_anagram/', AllUsersAnagramScores.as_view(), name='scoreboard_anagram'),
    path('scoreboard_math/', AllUsersMathScores.as_view(), name='scoreboard_math'),
    path('scoreboards_summary/',ScoreBoardsSummary.as_view(), name='scoreboards_summary')

]