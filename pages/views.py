from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'pages/home.html'

class AboutUsView(TemplateView):
    template_name = 'about-us.html'

class ContactUsView(TemplateView):
    template_name = 'contact-us.html'

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