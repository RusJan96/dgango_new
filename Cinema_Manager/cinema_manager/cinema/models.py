from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=100)
    duration = models.IntegerField(help_text="Duration in minutes")
    genre = models.CharField(max_length=100)
    release_date = models.DateField()

    def __str__(self):
        return self.title

class Hall(models.Model):
    name = models.CharField(max_length=100)
    capacity = models.IntegerField()

    def __str__(self):
        return self.name

class Session(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='sessions')
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE, related_name='sessions')
    show_time = models.DateTimeField()
    # price = models.DecimalField(null=True, default=0, max_digits=6, decimal_places=2, help_text="Price of the ticket in RUB")

    def __str__(self):
        return f"{self.movie.title} at {self.show_time} in {self.hall.name} on {self.price}"

# class Booking(models.Model):
#     session = models.ForeignKey(Session, on_delete=models.CASCADE, related_name='bookings')
#     customer_name = models.CharField(max_length=255)
#     number_of_tickets = models.IntegerField()
#     booking_time = models.DateTimeField(auto_now_add=True)

#     def total_price(self):
#         return self.number_of_tickets * self.session.price

#     def __str__(self):
#         return f"Booking by {self.customer_name} for {self.session.movie.title} on {self.session.show_time}"       
# Create your models here.
