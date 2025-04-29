from django.db import models
class MathFactsScoreBoard(models.Model):
    username = models.CharField(max_length=100, unique=True)
    mathfacts_score = [...]
