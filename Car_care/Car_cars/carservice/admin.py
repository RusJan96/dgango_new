from django.contrib import admin
from .models import AutoService, RepairType, ServiceRepair, Review

admin.site.register(AutoService)
admin.site.register(RepairType)
admin.site.register(ServiceRepair)
admin.site.register(Review)

# Register your models here.
