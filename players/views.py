from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.contrib.auth.models import User
from trades.models import Trade


class IndexView(LoginRequiredMixin, ListView):
    # Closed trade list by player
    queryset = Trade.objects.filter(
        date_closed__isnull=False).order_by('player', '-date_closed').distinct('player')
    context_object_name = 'player_trade_list'
    template_name = 'players/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # New player list
        context['new_player_list'] = User.objects.filter(
            groups__name='player', trade=None).order_by('-date_joined')
        return context


class PlayerView(LoginRequiredMixin, DetailView):
    context_object_name = 'player'
    template_name = 'players/player.html'

    def get_object(self):
        # Player
        player = get_object_or_404(User, username=self.kwargs['player_name'])
        return player

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        player = context['player']
        # Group list
        context['group_list'] = player.groups.all()
        # Opened trade list
        context['opened_trade_list'] = Trade.objects.filter(
            player=player, date_closed__isnull=True).order_by('-date_opened')
        # Closed trade list
        context['closed_trade_list'] = Trade.objects.filter(
            player=player, date_closed__isnull=False).order_by('-date_closed')
        return context


class ReturnsView(LoginRequiredMixin, ListView):
    context_object_name = 'trade_list'
    template_name = 'players/returns.html'

    def get_queryset(self):
        self.player = get_object_or_404(User, username=self.kwargs['player_name'])
        # Closed trade list
        trade_list = Trade.objects.filter(
            player=self.player, date_closed__isnull=False).order_by('-date_closed')
        return trade_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Player
        context['player'] = self.player
        # Group list
        context['group_list'] = self.player.groups.all()
        return context
