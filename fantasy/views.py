
from django.views.generic import TemplateView
from fantasy import models


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['teams'] = models.Team.objects.all()
        return context


class TeamView(TemplateView):
    template_name = 'team.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        team = self.request.GET.get('team')
        try:
            query = models.Team.objects.get(pk=team)
            context['players'] = query.players.all()
            context['team'] = query
        except models.Team.DoesNotExist:
            context['players'] = []

        return context
