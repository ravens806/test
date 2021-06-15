from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class WorkoutViews(TemplateView):
    template_name = 'workout.html'

class TacticsView(TemplateView):
    template_name = 'defence.html'

class TestView(TemplateView):
    template_name = 'base1-1.html'
class offballView(TemplateView):
    template_name = 'offball.html'