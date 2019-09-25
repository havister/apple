from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.views.generic import View, TemplateView
from django.contrib.auth.models import User
from trades.models import Trade


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'players/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Closed trade list by player
        context['player_trade_list'] = Trade.objects.filter(
            date_closed__isnull=False).order_by('player', '-date_closed').distinct('player')
        # New player list
        context['new_player_list'] = User.objects.filter(
            groups__name='player', trade=None).order_by('-date_joined')
        return context


class PlayerView(LoginRequiredMixin, TemplateView):
    template_name = 'players/player.html'

    def get(self, request, *args, **kwargs):
        if request.user.username != kwargs['player_name']:
            return redirect('players:index')
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Player
        player = self.request.user
        context['player'] = player
        # Group list
        context['group_list'] = player.groups.all()
        # Opened trade list
        context['opened_trade_list'] = Trade.objects.filter(
            player=player, date_closed__isnull=True).order_by('-date_opened')
        # Closed trade list
        context['closed_trade_list'] = Trade.objects.filter(
            player=player, date_closed__isnull=False).order_by('-date_closed')
        return context


class ReturnsView(LoginRequiredMixin, TemplateView):
    template_name = 'players/returns.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Player
        player = get_object_or_404(User, username=self.kwargs['player_name'])
        context['player'] = player
        # Group list
        context['group_list'] = player.groups.all()
        # Closed trade list
        context['trade_list'] = Trade.objects.filter(
            player=player, date_closed__isnull=False).order_by('-date_closed')
        return context
