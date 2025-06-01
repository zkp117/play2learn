from scoreboards.models import (
    MathFactsScoreBoard, 
    AnagramHuntScoreBoard, 
    MathFactsUserScores, 
    AnagramHuntUserScores
    )
from django.views.decorators.cache import never_cache
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views import View
from datetime import timedelta
import json
@method_decorator(never_cache, name='dispatch')
class MathFactsView(LoginRequiredMixin, TemplateView):
    template_name = "vue-templates/math-facts.html"
@method_decorator(never_cache, name='dispatch')
class AnagramHuntView(LoginRequiredMixin, TemplateView):
    template_name = "vue-templates/anagram-hunt.html"
@method_decorator(login_required, name='dispatch')
class EnterMathFactsScore(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            score = data.get('score')
            operation = data.get('operation')
            max_number = data.get('maxNumber')
            seconds_left = data.get('timeLeft')

            if None in (score, operation, max_number, seconds_left):
                return JsonResponse({'status': 'error', 'message': 'Missing data'}, status=400)
            
            MathFactsScoreBoard.objects.create(
                user = request.user,
                score = score,
                operation = operation,
                max_number = max_number,
                time_left = timedelta(seconds=float(seconds_left))
            )

            MathFactsUserScores.objects.create(
                user = request.user,
                score = score,
                operation = operation,
                max_number = max_number,
                time_left = timedelta(seconds=float(seconds_left))
            )
            return JsonResponse({'status': 'success'})
        except (json.JSONDecodeError, ValueError, TypeError) as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status = 400)
        
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
                user = request.user,
                score = score,
                word_length = word_length,
                time_left = timedelta(seconds=float(seconds_left))
            )

            AnagramHuntUserScores.objects.create(
                user = request.user,
                score = score,
                word_length = word_length,
                time_left = timedelta(seconds=float(seconds_left))
            )
            return JsonResponse({'status': 'success'})
        except (json.JSONDecodeError, ValueError, TypeError) as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status = 400)
        

        
