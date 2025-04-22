from django.shortcuts import render, get_object_or_404
from .models import AutoService, RepairType, ServiceRepair
from django.db.models import Q

def service_list(request):
    services = AutoService.objects.all()
    return render(request, 'carservice/service_list.html', {'services': services})

def service_detail(request, pk):
    service = get_object_or_404(AutoService, pk=pk)
    repairs = ServiceRepair.objects.filter(service=service)
    reviews = Review.objects.filter(service=service)
    return render(request, 'carservice/service_detail.html', {'service': service, 'repairs': repairs, 'reviews': reviews})


def select_repair(request):
    repair_types = RepairType.objects.all()
    if request.method == 'POST':
        form = RepairTypeForm(request.POST)
        if form.is_valid():
            selected_repair = form.cleaned_data['repair_type']
            services = AutoService.objects.filter(repairs__repair_type=selected_repair).distinct()
            return render(request, 'carservice/select_repair.html', {'services': services, 'selected_repair': selected_repair})
    else:
        form = RepairTypeForm()
    return render(request, 'carservice/select_repair.html', {'form': form, 'repair_types': repair_types})



# def select_repair(request):
#     repair_types = RepairType.objects.all()
#     if request.method == 'POST':
#         selected_repair_id = request.POST.get('repair_type')
#         selected_repair = get_object_or_404(RepairType, id=selected_repair_id)
#         services = AutoService.objects.filter(repairs__repair_type=selected_repair).distinct()
#         return render(request, 'carservice/select_repair.html', {'services': services, 'selected_repair': selected_repair})
#     return render(request, 'carservice/select_repair.html', {'repair_types': repair_types})
