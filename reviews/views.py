import html
from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView
from django.shortcuts import render

from common.utils.email_service import send_email
from .forms import ReviewsForm
class ReviewsAppView(FormView):
    template_name = 'reviews/write_review.html'
    form_class = ReviewsForm
    success_url = reverse_lazy('reviews:review_thanks')

    def user_review_view(request):
        form = ReviewsForm(request.POST or None)
        selected_game = request.POST.get('game') if request.method == 'POST' else None

        if selected_game == '2':
            pass

        elif selected_game == '3':
            pass

        else:
            pass

        return render(request, 'reviews/write_review.html', {'form': form})

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