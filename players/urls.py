from django.urls import path
from players.views import IndexView, PlayerView, ReturnsView

app_name = 'players'

urlpatterns = [
    # /players/
    path('', IndexView.as_view(), name='index'),
    # /players/player_name/
    path('<player_name>/', PlayerView.as_view(), name='player'),
    # /players/player_name/returns/
    path('<player_name>/returns/', ReturnsView.as_view(), name='returns'),
]
