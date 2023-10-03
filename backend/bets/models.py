from django.db import models
from users.models import User

# Create your models here.
class Bet(models.Model):
    # each bet will have two bettors, one referee, one winner, and one prize
    title = models.CharField(null=True, max_length=255)
    prompt = models.TextField(null=True, blank=True, max_length=255)
    bettor_1 = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='bettor_1_set')
    bettor_2 = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='bettor_2_set')
    referee = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='referee_set')
    winner = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='winner_set', blank=True)
    prize = models.TextField(null=True, blank=True, max_length=64)
    start = models.DateTimeField(null=True)
    end = models.DateTimeField(null=True, blank=True)