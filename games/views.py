from django.views.generic import TemplateView
class MathFactsView(TemplateView):
    template_name = "vue-templates/math-facts.html"

class AnagramHuntView(TemplateView):
    template_name = "vue-templates/anagram-hunt.html"
