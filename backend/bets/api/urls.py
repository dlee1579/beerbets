from django.urls import include, path
from rest_framework import routers
from bets.api.views import BetViewSet

router = routers.DefaultRouter()
# router.register(r'bets', BetViewSet, basename='bets')

urlpatterns = [
    path('', include(router.urls))
]
