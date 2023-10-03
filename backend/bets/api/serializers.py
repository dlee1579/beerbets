from rest_framework import serializers
from bets.models import Bet


class BetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bet
        fields = (
            'title',
            'prompt',
            'prize',
            'start',
            'end',
            'bettor_1',
            'bettor_2',
            'referee',
            'winner'
        )