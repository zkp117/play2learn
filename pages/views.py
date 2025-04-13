from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'pages/home.html'

class AboutUsView(TemplateView):
    template_name = 'pages/about_us.html'

class MyAccountView(TemplateView):
    template_name = 'account/my_account.html'

class AnagramHuntView(TemplateView):
    template_name = 'apps/AnagramHunt.vue'

class MathFactsView(TemplateView):
    template_name = 'apps/MathFacts.vue'