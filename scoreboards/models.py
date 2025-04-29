from django.db import models
from django.utils import timezone
import users.models
class MathFactsScoreBoard(models.Model):
    avatar = users.models.CustomUser.avatar
    username = users.models.AbstractUser.username
    mathfacts_score = users.models.CustomUser.mathfacts_score
    date_added = models.DateTimeField(('date added'), default=timezone.now)
class AnagramHuntScoreBoard(models.Model):
    avatar = users.models.CustomUser.avatar
    username = users.models.AbstractUser.username
    anagramhunt_score = users.models.CustomUser.anagramhunt_score
    date_added = models.DateTimeField(('date added'), default=timezone.now)

class ScoreBoardsSummary(models.Model):
    [...]
