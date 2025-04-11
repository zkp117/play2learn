from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.core.exceptions import ValidationError
from django.core.files.images import get_image_dimensions
from play2learn.storage_backends import PublicMediaStorage
from django.apps import apps

def validate_avatar(value):
    w, h = get_image_dimensions(value)
    if w > 500 or h > 500:
        raise ValidationError('Avatar must be no bigger than 500x500 pixels.')

class CustomUser(AbstractUser):

    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(('email address'), blank=True)
    dob = models.DateField(
        verbose_name="Date of Birth", null=True, blank=True
    )
    avatar = models.ImageField(upload_to='avatars/', 
            storage=PublicMediaStorage(), 
            blank=True, 
            null=True,
            validators = [validate_avatar])
    date_joined = models.DateTimeField(('date joined'), default=timezone.now)

    def get_anagramhunt_scores(self, obj):
        scores = obj.anagram_scores.all()
        total_score = sum(score.score for score in scores)
        return total_score

    def get_mathfacts_scores(self):
        return self.math_scores.aggregate(models.Sum('score'))['score_sum'] or 0

    def __str__(self):
        AnagramHuntScore = apps.get_model('games', 'AnagramHuntScore')
        MathFactsScore = apps.get_model('games', 'MathFactsScore')
        anagram_score_count = AnagramHuntScore.objects.filter(user=self).aggregate(models.Sum('score'))['score__sum'] or 0
        math_score_count = MathFactsScore.objects.filter(user=self).aggregate(models.Sum('score'))['score__sum'] or 0
        return f'{self.first_name} {self.last_name} ({self.username}) - Anagram Scores: {anagram_score_count}, Math Scores: {math_score_count}'

    def get_absolute_url(self):
        return reverse('my-account')


# user.anagramhuntscore_set.all()
# user.mathfactsscore_set.all()
