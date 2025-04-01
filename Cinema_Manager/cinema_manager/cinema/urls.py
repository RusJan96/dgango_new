from django.urls import path
from . import views

urlpatterns = [
    path('sessions/', views.upcoming_sessions, name='upcoming_sessions'),
    path('filter_sessions/', views.filter_sessions, name='filter_sessions'),
    path('hall/<int:hall_id>/sessions/', views.sessions_by_hall, name='sessions_by_hall'),
    path('session/<int:session_id>/book/', views.booking_view, name='booking_view'),
    path('movies/', views.movie_list, name='movie_list'),
    path('movies/<int:movie_id>/', views.movie_detail, name='movie_detail'),
    path('movies/add/', views.movie_create, name='movie_create'),
    path('movies/<int:movie_id>/edit/', views.movie_update, name='movie_update'),
    path('bookings/', views.booking_list, name='booking_list'),
    path('bookings/<int:booking_id>/', views.booking_detail, name='booking_detail'),
    path('session/<int:session_id>/book/', views.booking_create, name='booking_create'),
    path('bookings/<int:booking_id>/edit/', views.booking_update, name='booking_update'),
]