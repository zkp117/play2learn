import html
from .forms import ReviewsMathForm, ReviewsAnagramForm
from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import GameReviews

from common.utils.email_service import send_email
from .forms import ReviewsMathForm, ReviewsAnagramForm
class ReviewsMathAppView(LoginRequiredMixin, FormView):
    template_name = 'vue-reviews/reviewing_math.html'
    form_class = ReviewsMathForm
    success_url = reverse_lazy('vue-reviews:review_thanks')

    def form_valid(self, form):
        GameReviews.objects.create(
            user = self.request.user,
            game = 'mathfacts',
            review = form.cleaned_data['mathfacts_review']
        )


        data = form.cleaned_data
        to = 'neeneez2008@gmail.com'
        subject = 'Play2Learn Game Review'
        content = f'''<p>Your MathFacts review</p>
            <p>Game review received:</p>
            <p>{form.cleaned_data['mathfacts_review']}</p>
            <ol>'''
        for key, value in data.items():
            label = key.replace('_', ' ').title()
            entry = html.escape(str(value), quote=False)
            content += f'<li>{label}: {entry}</li>'
        
        content += '</ol>'

        send_email(to, subject, content)
        return super().form_valid(form)
    
class ReviewsAnagramAppView(LoginRequiredMixin, FormView):
    template_name = 'vue-reviews/reviewing_anagram.html'
    form_class = ReviewsAnagramForm
    success_url = reverse_lazy('vue-reviews:review_thanks')

    def form_valid(self, form):
        GameReviews.objects.create(
            user = self.request.user,
            game = 'anagramhunt',
            review = form.cleaned_data['anagramhunt_review']
        )

        data = form.cleaned_data
        to = 'neeneez2008@gmail.com'
        subject = 'Play2Learn Game Review'
        content = f'''<p>Your AnagramHunt review</p>
            <p>Game review received:</p>
            <p>{form.cleaned_data['anagramhunt_review']}</p>
            <ol>'''
        for key, value in data.items():
            label = key.replace('_', ' ').title()
            entry = html.escape(str(value), quote=False)
            content += f'<li>{label}: {entry}</li>'
        
        content += '</ol>'

        send_email(to, subject, content)
        return super().form_valid(form)


class ReviewsAppThanksView(TemplateView):
    template_name = 'vue-reviews/review_thanks.html'