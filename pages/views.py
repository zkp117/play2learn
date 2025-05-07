from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'pages/home.html'

class AboutUsView(TemplateView):
    template_name = 'pages/about_us.html'

class MyAccountView(TemplateView):
    template_name = 'account/my_account.html'

class AnagramHuntView(TemplateView):
    template_name = 'games/anagram-hunt.html'

class MathFactsView(TemplateView):
    template_name = 'games/math-facts.html'

class CustomLoginView(TemplateView):
    template_name = 'account/login.html'

class ScoreBoardsSummary(TemplateView):
    template_name = 'vue-scoreboards/scoreboards_summary.html'

class SettingsView(TemplateView):
    template_name = 'account/settings.html'