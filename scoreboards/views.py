from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import ( 
    MathFactsScoreBoard, 
    AnagramHuntScoreBoard, 
    MathFactsUserScores, 
    AnagramHuntUserScores )

@method_decorator(never_cache, name='dispatch')
class UserScores(LoginRequiredMixin, TemplateView):
    template_name = 'my_scores.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['mathfacts_userscores'] = MathFactsUserScores.objects.filter(user=user).order_by('-date_added')
        context['anagramhunt_userscores'] = AnagramHuntUserScores.objects.filter(user=user).order_by('-date_added')
        return context 
class ScoreBoards(LoginRequiredMixin, TemplateView):
    template_name = 'scoreboards.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mathfacts_scores'] = MathFactsScoreBoard.objects.order_by('-score')
        context['anagramhunt_scores'] = AnagramHuntScoreBoard.objects.order_by('-score')
        return context