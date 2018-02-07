from django.contrib import admin
from . import models

@admin.register(models.Player)
class PlayerAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Team)
class TeamAdmin(admin.ModelAdmin):
    pass

@admin.register(models.League)
class LeagueAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Fixture)
class FixtureAdmin(admin.ModelAdmin):
    pass

@admin.register(models.FantasyPlayer)
class FantasyPlayerAdmin(admin.ModelAdmin):
    pass