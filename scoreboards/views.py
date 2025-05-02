from django.views.generic import TemplateView
from .models import MathFactsScoreBoard, AnagramHuntScoreBoard
class ScoreBoards(TemplateView):
    template_name = 'templates/scoreboards.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # these display the top 10 scores for the mathfacts + anagramhunt scoreboards

        context['mathfacts_scores'] = MathFactsScoreBoard.objects.order_by('-score')[:10]

        context['anagramhunt_scores'] = AnagramHuntScoreBoard.objects.order_by('-score')[:10]

        return context





