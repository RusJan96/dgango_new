from django.contrib import admin
from .models import Movie, Hall, Session

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'duration', 'genre', 'release_date')

@admin.register(Hall)
class HallAdmin(admin.ModelAdmin):
    list_display = ('name', 'capacity')

@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    list_display = ('movie', 'hall', 'show_time')
    list_filter = ('movie', 'hall', 'show_time')

# @admin.register(Booking)
# class BookingAdmin(admin.ModelAdmin):
#     list_display = ('customer_name', 'session', 'number_of_tickets', 'booking_time', 'total_price')
#     list_filter = ('session__movie', 'session__hall', 'booking_time')
#     search_fields = ('customer_name',)    

# Register your models here.
