from django.urls import path
from .views import AllUsersAnagramScores, AllUsersMathScores

app_name = 'vue-scoreboards'

urlpatterns = [
    path('scoreboard_anagram/', AllUsersAnagramScores.as_view(), name='scoreboard_anagram'),
    path('scoreboard_math/', AllUsersMathScores.as_view(), name='scoreboard_math'),

]