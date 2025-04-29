from django.views.generic import TemplateView
class AllUsersMathScores(TemplateView):
    template_name = 'vue-scoreboards/scoreboard_math.html'
class AllUsersAnagramScores(TemplateView):
    template_name = 'vue-scoreboards/scoreboard_anagrams.html'

