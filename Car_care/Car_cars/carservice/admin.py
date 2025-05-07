from django.contrib import admin
from .models import AutoService, RepairType, ServiceRepair, Review, CarBrand, CarModel
from .forms import ServiceRepairForm

@admin.register(AutoService)
class AutoServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'rating')
    search_fields = ('name', 'address')
    list_filter = ('rating',)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('service', 'user', 'rating', 'created_at')
    list_filter = ('service', 'user', 'rating')
    search_fields = ('comment',)


class ServiceRepairAdmin(admin.ModelAdmin):
    form = ServiceRepairForm


# admin.site.register(AutoService)
admin.site.register(RepairType)
admin.site.register(CarModel)
# admin.site.register(Review)
admin.site.register(ServiceRepair, ServiceRepairAdmin)
admin.site.register(CarBrand)
# Register your models here.
