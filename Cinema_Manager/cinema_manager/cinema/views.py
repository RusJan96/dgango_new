from django.shortcuts import render
from .models import Movie, Hall, Session

def upcoming_sessions(request):
    sessions = Session.objects.select_related('movie', 'hall').all()
    return render(request, 'cinema/upcoming_sessions.html', {'sessions': sessions})

def filter_sessions(request):
    movie_id = request.GET.get('movie')
    hall_id = request.GET.get('hall')
    if movie_id:
        sessions = Session.objects.filter(movie_id=movie_id)
    elif hall_id:
        sessions = Session.objects.filter(hall_id=hall_id)
    else:
        sessions = Session.objects.all()
    return render(request, 'cinema/filter_sessions.html', {'sessions': sessions, 'movie_id': movie_id, 'hall_id': hall_id})

def sessions_by_hall(request, hall_id):
    sessions = Session.objects.filter(hall_id=hall_id)
    return render(request, 'cinema/sessions_by_hall.html', {'sessions': sessions, 'hall_id': hall_id})
# Create your views here.
