import json
from datetime import timedelta
from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views import View

from scoreboards.models import (
    MathFactsScoreBoard, 
    AnagramHuntScoreBoard, 
    MathFactsUserScores, 
    AnagramHuntUserScores
)

# --------------------
# Redirect Views for Vue Games
# --------------------
@method_decorator(login_required, name='dispatch')
class MathFactsView(TemplateView):
    template_name = "vue-templates/math-facts.html"
@method_decorator(login_required, name='dispatch')
class AnagramHuntView(TemplateView):
    template_name = "vue-templates/anagram-hunt.html"

# --------------------
# Score Recording APIs
# --------------------
@method_decorator(login_required, name='dispatch')
class EnterMathFactsScore(View):
    def post(self, request):
        try:
            data = json.loads(request.body)pt.6
            score = data.get('score')
            operation = data.get('operation')
            max_number = data.get('maxNumber')
            seconds_left = data.get('timeLeft')

            if None in (score, operation, max_number, seconds_left):
                return JsonResponse({'status': 'error', 'message': 'Missing data'}, status=400)
            
            MathFactsScoreBoard.objects.create(
                user=request.user,
                score=score,
                operation=operation,
                max_number=max_number,
                time_left=timedelta(seconds=float(seconds_left))
            )
            MathFactsUserScores.objects.create(
                user=request.user,
                score=score,
                operation=operation,
                max_number=max_number,
                time_left=timedelta(seconds=float(seconds_left))
            )
            return JsonResponse({'status': 'success'})
        except (json.JSONDecodeError, ValueError, TypeError) as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)

@method_decorator(login_required, name='dispatch')
class EnterAnagramHuntScore(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            score = data.get('score')
            word_length = data.get('wordLength')
            seconds_left = data.get('timeLeft')

            if None in (score, word_length, seconds_left):
                return JsonResponse({'status': 'error', 'message': 'Missing data'}, status=400)
            
            AnagramHuntScoreBoard.objects.create(
                user=request.user,
                score=score,
                word_length=word_length,
                time_left=timedelta(seconds=float(seconds_left))
            )
            AnagramHuntUserScores.objects.create(
                user=request.user,
                score=score,
                word_length=word_length,
                time_left=timedelta(seconds=float(seconds_left))
            )
            return JsonResponse({'status': 'success'})
        except (json.JSONDecodeError, ValueError, TypeError) as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)

# --------------------
# Utility Endpoint
# --------------------

def is_logged_in(request):
    if request.user.is_authenticated:
        return JsonResponse({'logged_in': True, 'username': request.user.username})
    else:
        return JsonResponse({'logged_in': False})