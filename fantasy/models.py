from __future__ import unicode_literals

from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=100)
    league = models.ForeignKey('League', related_name='teams')
    reference_id = models.CharField(max_length=10)
    logo = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        unique_together = ('reference_id', 'league')


class Player(models.Model):
    team = models.ForeignKey(Team, related_name='players')
    name = models.CharField(max_length=100)
    number = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    image = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class League(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Fixture(models.Model):
    home = models.OneToOneField(Team, related_name='home_team')
    away = models.OneToOneField(Team, related_name='away')
    kick_off = models.DateTimeField()
    home_score = models.IntegerField(default=0)
    away_score = models.IntegerField(default=0)

    def __str__(self):
        return '%s vs %s' % (self.home, self.away)

class FantasyPlayer(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name