from django.urls import path
from . import views

urlpatterns = [
    path('',views.WorkoutViews.as_view(),name='workout'), #top
    path('tactics/',views.TacticsView.as_view(),name='defence'),#tactics
    path('tes/',views.TestView.as_view(),name='test'),
    path('offball/',views.offballView.as_view(),name='offball'),
]