from django.urls import path
from . import views

urlpatterns = [
    path('sessions/', views.upcoming_sessions, name='upcoming_sessions'),
    path('filter_sessions/', views.filter_sessions, name='filter_sessions'),
    path('hall/<int:hall_id>/sessions/', views.sessions_by_hall, name='sessions_by_hall'),
]