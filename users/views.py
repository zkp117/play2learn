from django.contrib.auth import get_user_model
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from .forms import CustomAuthenticationForm, CustomUserChangeForm, CustomSignupForm
from reviews.models import GameReviews
from allauth.account.views import SignupView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView as DjangoPasswordChangeView, LoginView, PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin

from django.urls import reverse_lazy
import random

from django.views.generic import UpdateView

from scoreboards.models import AnagramHuntScoreBoard, MathFactsScoreBoard
class CustomPasswordChangeView(SuccessMessageMixin, LoginRequiredMixin, DjangoPasswordChangeView):
    success_url = reverse_lazy('my-account')
    login_url = reverse_lazy('account_login')
    
class MyAccountPageView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = get_user_model()
    login_url = reverse_lazy('account_login')
    form_class = CustomUserChangeForm
    success_message = 'Update Successful'
    success_url = reverse_lazy('my-account')
    template_name = 'account/my_account.html'

    def get_object(self):
        return self.request.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user

        # Fetch AnagramHunt and MathFacts scores
        anagram_scores = AnagramHuntScoreBoard.objects.filter(user=user)
        mathfacts_scores = MathFactsScoreBoard.objects.filter(user=user)

        # AnagramHunt scores (newest + highest)
        context['anagramhunt_newest'] = anagram_scores.order_by('-date_added').first()
        context['anagramhunt_highest'] = anagram_scores.order_by('-score').first()

        # MathFacts scores (newest + highest)
        context['mathfacts_newest'] = mathfacts_scores.order_by('-date_added').first()
        context['mathfacts_highest'] = mathfacts_scores.order_by('-score').first()

        # MathFacts and AnagramHunt reviews (recent)
        context['anagramreview_newest'] = GameReviews.objects.filter(user=user, game='anagramhunt').order_by('-submitted').first()
        context['mathreview_newest'] = GameReviews.objects.filter(user=user, game='mathfacts').order_by('-submitted').first()

        return context
class PasswordEmailView(PasswordResetView):
    def get_email_context(self, context): 
        context['domain'] = '127.0.0.1:8000'
        context['site_name'] = 'Play2Learn'
        context['protocol'] = 'http'
        return context

@login_required
def clear_avatar(request):
    user = request.user
    user.avatar.delete()
    user.save()
    return redirect('my-account') 
class CustomLoginView(LoginView):
    template_name = 'account/login.html'
    authentication_form = CustomAuthenticationForm

    def get_success_url(self):
        return reverse_lazy('my-account')
    
class CustomSignupView(SignupView):
    template_name = 'account/signup.html'
    form_class = CustomSignupForm

    def get_success_url(self):
        return reverse_lazy('my-account')

def homepage_view(request):
    reviews = list(GameReviews.objects.all())
    random_reviews = random.sample(reviews, min(3, len(reviews))) if reviews else []
    return render(request, 'pages/home.html', {'random_reviews': random_reviews})