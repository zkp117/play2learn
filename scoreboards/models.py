from django.db import models
from django.utils import timezone
from users.models import CustomUser
class MathFactsScoreBoard(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)
    date_added = models.DateTimeField(('date added'), default=timezone.now)
class AnagramHuntScoreBoard(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)
    date_added = models.DateTimeField(('date added'), default=timezone.now)