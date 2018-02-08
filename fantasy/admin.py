from django.contrib import admin
from django.utils.html import format_html

from . import models


@admin.register(models.Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('name', 'thumbnail', 'position', 'team')
    list_filter = ('team',)

    def thumbnail(self, obj):
        return format_html('<img src="%s" style="height:50px;width: 50px"/>' % obj.image)


@admin.register(models.Team)
class TeamAdmin(admin.ModelAdmin):
     list_display = ('name', 'thumbnail', 'league')

     def thumbnail(self, obj):
        return format_html('<img src="%s" style="height:50px;width: 50px"/>' % obj.logo)


@admin.register(models.League)
class LeagueAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Fixture)
class FixtureAdmin(admin.ModelAdmin):
    pass


@admin.register(models.FantasyPlayer)
class FantasyPlayerAdmin(admin.ModelAdmin):
    pass