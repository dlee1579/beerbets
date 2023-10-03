from django.urls import include, path
from rest_framework import routers
# import users
from users.api.views import UserViewSet
from bets.api.views import BetViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet, basename='users')
router.register(r'bets', BetViewSet, basename='bets')
# router.register

urlpatterns = [
    path('', include(router.urls))
    # path('users/', include(users.api.urls))
]
