from django.db import models
from django.urls import reverse
from users.models import CustomUser
from common.utils.text import unique_slug
import datetime
class Category(models.Model):
    category = models.CharField(max_length=50)
    slug = models.SlugField(
        max_length=50, unique=True, null=False, editable=False
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('scores:category', args=[self.slug])

    def save(self, *args, **kwargs):
        if not self.slug:
            value = self.category
            self.slug = unique_slug(value, type(self))
        super().save(*args, **kwargs)

    def __str__(self):
        return self.category
class AnagramHuntScore(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='anagram_scores')
    score = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    word_length = models.IntegerField(null=True, blank=True)
    time_left = models.DurationField(default=datetime.timedelta(seconds=0))

    def __str__(self):
        return f"{self.user} - AnagramHunt : {self.score}"
    
    @property
    def leading_score(self):
        return AnagramHuntScore.objects.filter(user=self.user).order_by('-score').first()
class MathFactsScore(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='math_scores')
    score = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    operation = models.CharField(max_length=20, blank=True)
    max_number = models.IntegerField(null=True, blank=True)
    time_left = models.DurationField(default=datetime.timedelta(seconds=0))


    def __str__(self):
        return f"{self.user} - MathFacts : {self.score}"

    @property
    def leading_score(self):
        return MathFactsScore.objects.filter(user=self.user).order_by('-score').first()
class AnagramReview(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='anagram_reviews')
    review_text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review for AnagramHunt by {self.user.username}"

class MathReview(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='math_reviews')
    review_text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review for MathFacts by {self.user.username}"

