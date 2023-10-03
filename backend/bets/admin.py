from bets.models import Bet
from django.contrib import admin

# Register your models here.
@admin.register(Bet)
class BetAdmin(admin.ModelAdmin):
    pass