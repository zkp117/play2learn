from django.views.generic import TemplateView
from .models import MathFactsScoreBoard, AnagramHuntScoreBoard, MathFactsUserScores, AnagramHuntUserScores
class ScoreBoards(TemplateView):
    template_name = 'scoreboards.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['mathfacts_scores'] = MathFactsScoreBoard.objects.order_by('-score')[:10]
        context['anagramhunt_scores'] = AnagramHuntScoreBoard.objects.order_by('-score')[:10]

        return context

class UserScores(TemplateView):
    template_name = 'my_scores.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['mathfacts_scores'] = MathFactsUserScores.objects.order_by('-date_added')
        context['anagramhunt_scores'] = AnagramHuntUserScores.objects.order_by('-date_added')


def render_to_response(self, context, **response_kwargs):
        response = super().render_to_response(context, **response_kwargs)
        
        # Explicitly disable caching
        response['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
        response['Pragma'] = 'no-cache'
        response['Expires'] = '0'

        return response
