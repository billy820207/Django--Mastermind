from mastermind.models import Game, Guess
from django.contrib import admin

class GameAdmin(admin.ModelAdmin):




admin.site.register(Game)
admin.site.register(Guess)