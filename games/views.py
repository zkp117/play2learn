from django.views.generic import TemplateView
class MathFactsView(TemplateView):
    template_name = "apps/math-facts.html"
class AnagramHuntView(TemplateView):
    template_name = "apps/anagram-hunt.html"