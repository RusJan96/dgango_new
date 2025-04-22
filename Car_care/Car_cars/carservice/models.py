from django.db import models
from django.contrib.auth.models import User
# from .models import AutoService

class AutoService(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=0.0)

    def __str__(self):
        return self.name

class RepairType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class ServiceRepair(models.Model):
    service = models.ForeignKey(AutoService, on_delete=models.CASCADE, related_name='repairs')
    repair_type = models.ForeignKey(RepairType, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.repair_type.name} - {self.price} руб."

class Review(models.Model):
    service = models.ForeignKey(AutoService, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    rating = models.IntegerField()

    def __str__(self):
        return f"Review by {self.user.username} for {self.service.name}"     


# Create your models here.
