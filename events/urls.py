from django.urls import path
from events.views import IndexView

app_name = 'events'

urlpatterns = [
    # /events/havister/
    path('havister/', IndexView.as_view(), name='havister'),
]
