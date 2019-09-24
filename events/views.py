from django.shortcuts import render
from django.urls import reverse
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'events/havister.html'
