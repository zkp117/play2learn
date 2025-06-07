from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.core.exceptions import ValidationError
from django.core.files.images import get_image_dimensions
from django.views.decorators.cache import never_cache
from play2learn.storage_backends import PublicMediaStorage

def validate_avatar(value):
    w, h = get_image_dimensions(value)
    if w > 200 or h > 200:
        raise ValidationError('Avatar must be no bigger than 200x200 pixels.')
class CustomUser(AbstractUser):
    username = models.CharField(max_length=100, unique=True,
        verbose_name= 'Username')
    email = models.EmailField(('email address'), blank=True)
    dob = models.DateField(
        verbose_name="Date of Birth", null=True, blank=True,
    )
    avatar = models.ImageField(upload_to='avatars/', 
        storage=PublicMediaStorage(), 
        blank=True, 
        null=True,
        validators = [validate_avatar],
        help_text= 'Avatar cannot be larger than 200x200 pixels',)
    date_joined = models.DateTimeField(('date joined'), default=timezone.now)

    # Score fields
    anagramhunt_score = models.IntegerField(default=0)
    mathfacts_score = models.IntegerField(default=0)

    # Reivew fields
    anagramhunt_reviews = models.TextField(null=True, blank=True)
    mathfacts_reviews = models.TextField(null=True, blank=True)

    def get_anagramhunt_scores(self):
        return self.anagram_scores.aggregate(models.Sum('score'))['score_sum'] or 0

    def get_mathfacts_scores(self):
        return self.math_scores.aggregate(models.Sum('score'))['score_sum'] or 0
    
    # shows only username in 'user' section in 'scoreboards' section in admin
    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('my-account')
