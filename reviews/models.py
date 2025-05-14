from django.db import models
from django.conf import settings

class GameReviews(models.Model):
    GAME_CHOICES = [
        ('mathfacts', 'MathFacts'),
        ('anagramhunt', 'AnagramHunt'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='game_reviews')
    game = models.CharField(max_length=20, choices=GAME_CHOICES)
    review = models.TextField()
    submitted = models.DateTimeField(auto_now_add=True)

    def __st__(self):
        return f"{self.user.username} - {self.get_game_display()}"