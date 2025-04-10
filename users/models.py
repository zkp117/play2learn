from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.core.exceptions import ValidationError
from django.core.files.images import get_image_dimensions
from play2learn.storage_backends import PublicMediaStorage

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

    def anagramhunt_scores(self):
        return self.anagramhunt_scores.aggregate(models.Sum('score'))['score_sum'] or 0
    
    def mathfacts_scores(self):
        return self.mathfacts_scores.aggregate(models.Sum('score'))['score_sum'] or 0

    def __str__(self):
        anagram_score_count = self.anagram_scores.count()
        math_score_count = self.math_scores.count()
        return f'{self.first_name} {self.last_name} ({self.username}) - Anagram Scores: {anagram_score_count}, Math Scores: {math_score_count}'


    def get_absolute_url(self):
        return reverse('my-account')


# user.anagramhuntscore_set.all()
# user.mathfactsscore_set.all()
