from django.db import models
# from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.utils import timezone
from django.conf import settings
# from .models import AutoService


# class User(AbstractUser):

#   firstname = models.CharField(max_length=100, verbose_name='Имя')
#   lastname = models.CharField(max_length=100, verbose_name='Фамилия')

#   def __str__(self):
#     return self.username

class CarBrand(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class CarModel(models.Model):
    brand = models.ForeignKey(CarBrand, on_delete=models.CASCADE, related_name='models')
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.brand.name} {self.name}"        


class AutoService(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=0.0)
    address = models.CharField(null=True)
    car_brands = models.ManyToManyField(CarBrand, related_name='autoservices')
    # repairs = models.ManyToManyField(RepairType, related_name='autoservices')
    def __str__(self):
        return self.name

    
    def update_rating(self):
        reviews = self.reviews.all()
        if reviews.exists():
            self.rating = reviews.aggregate(models.Avg('rating'))['rating__avg']
        else:
            self.rating = 0.0
        self.save()    

class RepairType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class ServiceRepair(models.Model):
    service = models.ForeignKey(AutoService, on_delete=models.CASCADE, related_name='repairs')
    repair_type = models.ForeignKey(RepairType, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.IntegerField(help_text="Время работы в часах", default=1)

    def __str__(self):
        return f"{self.repair_type.name} - {self.price} руб.({self.duration} ч)"

class Review(models.Model):
    service = models.ForeignKey(AutoService, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # user = models.ForeignKey(
    #     settings.AUTH_USER_MODEL,
    #     on_delete=models.CASCADE,
    #     related_name='reviews'
    # )
    
    comment = models.TextField()
    rating = models.IntegerField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Review by {self.user.username} for {self.service.name}"     



# Create your models here.
