from rest_framework import viewsets
from bets.api.serializers import BetSerializer
from bets.models import Bet

class BetViewSet(viewsets.ModelViewSet):
    serializer_class = BetSerializer
    
    def get_queryset(self):
        return Bet.objects.all()
    