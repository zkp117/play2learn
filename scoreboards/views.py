from django.views.generic import TemplateView
class AllUsersMathScores(TemplateView):
    template_name = 'vue-scorebaords/scoreboard_math.html'
class AllUsersAnagramScores(TemplateView):
    template_name = 'vue-scorebaords/scoreboard_anagrams.html'

