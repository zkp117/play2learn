from django.db import models
from django.conf import settings
from django.utils import timezone
from users.models import CustomUser
class MathFactsScoreBoard(models.Model):
    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='math_scores')
    score = models.IntegerField(default=0)
    operation = models.CharField()
    max_number = models.IntegerField() 
    time_left = models.DurationField()
    date_added = models.DateTimeField(('date added'), default=timezone.now)

    @property
    def seconds_left(self):
        return int(self.time_left.total_seconds())

    def __str__(self):
        return self.user.username
class AnagramHuntScoreBoard(models.Model):
    user = models.ForeignKey(
        CustomUser, 
        on_delete=models.CASCADE,
        related_name='anagram_scores')
    score = models.IntegerField(default=0)
    word_length = models.IntegerField()
    time_left = models.DurationField()
    date_added = models.DateTimeField(('date added'), default=timezone.now)

    @property
    def seconds_left(self):
        return int(self.time_left.total_seconds())

    def __str__(self):
        return self.user.username
class MathFactsUserScores(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE)
    score = models.IntegerField(default=0)
    operation = models.CharField(max_length=100)
    max_number = models.IntegerField() 
    time_left = models.DurationField()
    date_added = models.DateTimeField(('date added'), default=timezone.now)

    @property
    def seconds_left(self):
        return int(self.time_left.total_seconds())
class AnagramHuntUserScores(models.Model):
    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE)
    score = models.IntegerField(default=0)
    word_length = models.IntegerField()
    time_left = models.DurationField()
    date_added = models.DateTimeField(('date added'), default=timezone.now)
    
    @property
    def seconds_left(self):
        return int(self.time_left.total_seconds())