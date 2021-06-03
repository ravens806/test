from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class WorkoutViews(TemplateView):
    template_name = 'workout.html'

class TacticsView(TemplateView):
    template_name = 'tactics.html'

class TestView(TemplateView):
    template_name = 'base1-1.html'