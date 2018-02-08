from django.core.management.base import BaseCommand

from fantasy.scrapers.website import premier_league


class Command(BaseCommand):
    def handle(self, *args, **options):
        premier_league.main()
