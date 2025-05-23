import html
from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import GameReviews
from common.utils.email_service import send_email
from .forms import ReviewsMathForm, ReviewsAnagramForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

@method_decorator(login_required, name='dispatch')
class ReviewsMathAppView(LoginRequiredMixin, FormView):
    template_name = 'vue-reviews/reviewing_math.html'
    form_class = ReviewsMathForm
    success_url = reverse_lazy('vue-reviews:review_thanks')

    def form_valid(self, form):
        review_text = form.cleaned_data['mathfacts_reviews']

        GameReviews.objects.create(
            user=self.request.user,
            game='mathfacts',
            review=review_text
        )

        self.request.user.mathfacts_reviews = review_text
        self.request.user.save()

        # Send email
        data = form.cleaned_data
        to = 'neeneez2008@gmail.com'
        subject = 'Play2Learn Game Review - MathFacts'
        content = f'''<p>Your MathFacts review</p>
        <p>Game review received:</p>
        <p>{html.escape(review_text)}</p>
        <ol>'''
        for key, value in data.items():
            label = key.replace('_', ' ').title()
            entry = html.escape(str(value), quote=False)
            content += f'<li>{label}: {entry}</li>'
        content += '</ol>'

        send_email(to, subject, content)

        return super().form_valid(form)
@method_decorator(login_required, name='dispatch')
class ReviewsAnagramAppView(LoginRequiredMixin, FormView):
    template_name = 'vue-reviews/reviewing_anagram.html'
    form_class = ReviewsAnagramForm
    success_url = reverse_lazy('vue-reviews:review_thanks')

    def form_valid(self, form):
        review_text = form.cleaned_data['anagramhunt_reviews']

        # Save to GameReviews
        GameReviews.objects.create(
            user=self.request.user,
            game='anagramhunt',
            review=review_text
        )

        self.request.user.anagramhunt_reviews = review_text
        self.request.user.save()

        # Send email
        data = form.cleaned_data
        to = 'neeneez2008@gmail.com'
        subject = 'Play2Learn Game Review - AnagramHunt'
        content = f'''<p>Your AnagramHunt review</p>
        <p>Game review received:</p>
        <p>{html.escape(review_text)}</p>
        <ol>'''
        for key, value in data.items():
            label = key.replace('_', ' ').title()
            entry = html.escape(str(value), quote=False)
            content += f'<li>{label}: {entry}</li>'
        content += '</ol>'

        send_email(to, subject, content)

        return super().form_valid(form)

@method_decorator(login_required, name='dispatch')
class ReviewsAppThanksView(TemplateView):
    template_name = 'vue-reviews/review_thanks.html'
