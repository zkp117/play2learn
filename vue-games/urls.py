from django.urls import path
from django.views.generic import TemplateView

app_name = 'vue-games'

urlpatterns = [
    path('math-facts/', TemplateView.as_view(template_name="vue-templates/math-facts.html"), name='math-facts'),
    path('anagram-hunt/', TemplateView.as_view(template_name="vue-templates/anagram-hunt.html"), name='anagram-hunt'),
]
