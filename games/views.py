from .models import MathFactsScore, AnagramHuntScore
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views import View
import json
class MathFactsView(TemplateView):
    template_name = "vue-templates/math-facts.html"

class AnagramHuntView(TemplateView):
    template_name = "vue-templates/anagram-hunt.html"
@method_decorator(login_required, name='dispatch')
class EnterMathFactsScore(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            score = data.get('score')
            if score is not None:
                MathFactsScore.objects.create(user=request.user, score=score)
                return JsonResponse({'status': 'success', 'score': score})
            else:
                return JsonResponse({'status': 'error', 'message': 'No score provided'}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({'status': 'error', 'message': 'Invalid JSON'}, status=400)
    
@method_decorator(csrf_exempt, name='dispatch')
@method_decorator(login_required, name='dispatch')
class EnterAnagramHuntScore(View): [...]