from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView

from .forms import ReviewForm
class ReviewsAppView(FormView):
    template_name = 'reviews/write_review.html'
    form_class = ReviewsForm
    success_url = reverse_lazy('reviews:thanks')

class ReviewsAppThanksView(TemplateView):
    template_name = 'reviews/thanks_review.html'