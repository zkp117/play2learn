from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import MathFactsScoreBoard, AnagramHuntScoreBoard, MathFactsUserScores, AnagramHuntUserScores
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

@method_decorator(login_required, name='dispatch')
class ScoreBoards(TemplateView):
    template_name = 'scoreboards.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['mathfacts_scores'] = MathFactsScoreBoard.objects.order_by('-score')[:10]
        context['anagramhunt_scores'] = AnagramHuntScoreBoard.objects.order_by('-score')[:10]

        return context
@method_decorator(login_required, name='dispatch')
class UserScores(LoginRequiredMixin, TemplateView):
    template_name = 'my_scores.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['mathfacts_userscores'] = MathFactsUserScores.objects.filter(user=user).order_by('-date_added')
        context['anagramhunt_userscores'] = AnagramHuntUserScores.objects.filter(user=user).order_by('-date_added')
        return context 


def render_to_response(self, context, **response_kwargs):
        response = super().render_to_response(context, **response_kwargs)
        
        # Explicitly disable caching
        response['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
        response['Pragma'] = 'no-cache'
        response['Expires'] = '0'

        return response
