from django.db import models
from django.urls import reverse
from users.models import CustomUser

from common.utils.text import unique_slug
class Category(models.Model):
    category = models.CharField(max_length=50)
    slug = models.SlugField(
        max_length=50, unique=True, null=False, editable=False
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('jokes:category', args=[self.slug])

    def save(self, *args, **kwargs):
        if not self.slug:
            value = str(self)
            self.slug = unique_slug(value, type(self))
        super().save(*args, **kwargs)

    def __str__(self):
        return self.category
    
class AnagramHuntScore(models.Model): 
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='anagram_scores')
    score = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)

class MathFactsScore(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='math_scores')
    score = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
