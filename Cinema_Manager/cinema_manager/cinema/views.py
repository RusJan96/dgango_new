from django.shortcuts import render, get_object_or_404, redirect
from .models import Movie, Hall, Session, Booking
from .forms import MovieForm, BookingForm

def booking_list(request):
    bookings = Booking.objects.all()
    return render(request, 'cinema/booking_list.html', {'bookings': bookings})

def booking_detail(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    return render(request, 'cinema/booking_detail.html', {'booking': booking})

def booking_create(request, session_id):
    session = get_object_or_404(Session, id=session_id)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.session = session
            booking.save()
            return redirect('booking_detail', booking_id=booking.id)
    else:
        form = BookingForm()
    return render(request, 'cinema/booking_form.html', {'form': form, 'title': 'Add Booking'})

def booking_update(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            booking = form.save()
            return redirect('booking_detail', booking_id=booking.id)
    else:
        form = BookingForm(instance=booking)
    return render(request, 'cinema/booking_form.html', {'form': form, 'title': 'Edit Booking'})



def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'cinema/movie_list.html', {'movies': movies})

def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    return render(request, 'cinema/movie_detail.html', {'movie': movie})

def movie_create(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('movie_list')
    else:
        form = MovieForm()
    return render(request, 'cinema/movie_form.html', {'form': form, 'title': 'Add Movie'})

def movie_update(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    if request.method == 'POST':
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('movie_detail', movie_id=movie.id)
    else:
        form = MovieForm(instance=movie)
    return render(request, 'cinema/movie_form.html', {'form': form, 'title': 'Edit Movie'})



def booking_view(request, session_id):
    session = get_object_or_404(Session, id=session_id)
    if request.method == 'POST':
        customer_name = request.POST.get('customer_name')
        number_of_tickets = int(request.POST.get('number_of_tickets'))
        booking = Booking.objects.create(
            session=session,
            customer_name=customer_name,
            number_of_tickets=number_of_tickets
        )
        return render(request, 'cinema/booking_success.html', {'booking': booking})
    return render(request, 'cinema/booking.html', {'session': session})

    
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
