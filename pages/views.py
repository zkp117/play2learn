from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache

@method_decorator(never_cache, name='dispatch')
class HomePageView(TemplateView):
    template_name = 'pages/home.html'

class AboutUsView(TemplateView):
    template_name = 'about-us.html'

class MyAccountView(TemplateView):
    template_name = 'account/my-account.html'

class AnagramHuntView(TemplateView):
    template_name = 'games/anagram-hunt.html'

class MathFactsView(TemplateView):
    template_name = 'games/math-facts.html'

class CustomLoginView(TemplateView):
    template_name = 'account/login.html'

class MyScoresView(TemplateView):
    template_name = 'my_scores.html'

class ScoreBoardsView(TemplateView):
    template_name = 'templates/scoreboards.html'