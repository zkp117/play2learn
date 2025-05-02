from django.views.generic import TemplateView
from games.models import MathFactsScore, AnagramHuntScore
class ScoreBoards(TemplateView):
    template_name = 'scoreboards.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['mathfacts_scores'] = MathFactsScore.objects.order_by('-score')[:10]
        context['anagramhunt_scores'] = AnagramHuntScore.objects.order_by('-score')[:10]

        return context




