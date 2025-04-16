import html
from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView

from common.utils.email_service import send_email
from .forms import ReviewsForm
class ReviewsAppView(FormView):
    template_name = 'reviews/write_views.html'
    form_class = ReviewsForm
    success_url = reverse_lazy('reviews:review_thanks')

    def form_valid(self, form):
        data = form.cleaned_data
        to = 'neeneez2008@gmail.com'
        subject = 'Play2Learn Game Review'
        content = f'''<p>Your {'game_choices'} review</p>
            <p>Game review received:</p>
            <ol>'''
        for key, value in data.items():
            label = key.replace('_', ' ').title()
            entry = html.escape(str(value), quote=False)
            content += f'<li>{label}: {entry}</li>'
        
        content += '</ol>'

        send_email(to, subject, content)
        return super().form_valid(form)

class ReviewsAppThanksView(TemplateView):
    template_name = 'reviews/review_thanks.html'