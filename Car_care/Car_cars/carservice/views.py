from django.shortcuts import render, get_object_or_404, redirect
from .models import AutoService, RepairType, ServiceRepair, CarBrand, CarModel, Review
from .forms import ServiceSearchForm, ReviewForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q


def service_list(request):
    form = ServiceSearchForm(request.GET)
    services = AutoService.objects.all()
    car_brand = None
    car_model = None
    repair_type = None

    if form.is_valid():
        car_brand = form.cleaned_data.get('car_brand')
        car_model = form.cleaned_data.get('car_model')
        repair_type = form.cleaned_data.get('repair_type')

        if car_brand:
            services = services.filter(car_brands=car_brand)
        if car_model:
            services = services.filter(car_models=car_model)
        if repair_type:
        #    try:
                service_repair = ServiceRepair.objects.filter(repair_type=repair_type)
                auto_services = set()
                for repair in service_repair:
                    auto_services.add(repair.service)

                auto_services = list(auto_services)
                services = auto_services
            # except ServiceRepair.DoesNotExist:
            #     services = services.none()

    sort_by = request.GET.get('sort', 'rating')
    if sort_by == 'rating':
        services = services.order_by('-rating')
    else:
        services = services.order_by('name')

    return render(request, 'carservice/service_list.html', {
        'services': services,
        'form': form,
        'car_brand': car_brand,
        'car_model': car_model,
        'repair_type': repair_type
    })
    
    # return render(request, 'carservice/service_list.html', {'services': services})


    #  # Обработка сортировки
    # sort_by = request.GET.get('sort', 'name')  # По умолчанию сортируем по названию
    # if sort_by == 'rating':
    #     services = services.order_by('-rating', 'name')  # Сортировка по убыванию рейтинга, затем по названию
    # else:
    #     services = services.order_by('name')  # Сортировка по названию

    # context = {
    #     'form': form,
    #     'services': services,
    # }
    # return render(request, 'service_list.html', context)




# ВРЕМЕННО!! ИЗМЕНИ ФОРМУ ДЛЯ ТОГО ЧТОБЫ ВЫВОДИТЬ МАРКУ И МОДЕЛЬ АВТОМОБИЛЯ!
# def service_list(request):
#     form = ServiceSearchForm(request.GET)
#     services = AutoService.objects.all()
#     if form.is_valid():
#         car_brand = form.cleaned_data.get('car_brand')
#         repair_type = form.cleaned_data.get('repair_type')
#         if car_brand:
#             services = services.filter(car_brands=car_brand)
#         if repair_type:
#             services = services.filter(repairs__repair_type=repair_type)
#     return render(request, 'carservice/service_list.html', {'services': services, 'form': form})



# def service_list(request):
#     services = AutoService.objects.all()
#     return render(request, 'carservice/service_list.html', {'services': services})
 

def service_detail(request, pk):
    service = get_object_or_404(AutoService, pk=pk)
    repairs = ServiceRepair.objects.filter(service=service)
    reviews = Review.objects.filter(service=service)
    if request.method == 'POST':
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.service = service
            review.user = request.user
            review.save()
            service.update_rating()
            return redirect('service_detail', pk=service.pk)
    else:
        review_form = ReviewForm()
    return render(request, 'carservice/service_detail.html', {
        'service': service,
        'repairs': repairs,
        'reviews': reviews,
        'review_form': review_form
    })

# def service_detail(request, pk):
#     service = get_object_or_404(AutoService, pk=pk)
#     repairs = ServiceRepair.objects.filter(service=service)
#     reviews = Review.objects.filter(service=service)[:3]
#     return render(request, 'carservice/service_detail.html', {'service': service, 'repairs': repairs, 'reviews': reviews})



# def select_repair(request):
#     repair_types = RepairType.objects.all()
#     if request.method == 'POST':
#         form = RepairTypeForm(request.POST)
#         if form.is_valid():
#             selected_repair = form.cleaned_data['repair_type']
#             services = AutoService.objects.filter(repairs__repair_type=selected_repair).distinct()
#             return render(request, 'carservice/select_repair.html', {'services': services, 'selected_repair': selected_repair})
#     else:
#         form = RepairTypeForm()
#     return render(request, 'carservice/select_repair.html', {'form': form, 'repair_types': repair_types})



# def select_repair(request):
#     repair_types = RepairType.objects.all()
#     if request.method == 'POST':
#         selected_repair_id = request.POST.get('repair_type')
#         selected_repair = get_object_or_404(RepairType, id=selected_repair_id)
#         services = AutoService.objects.filter(repairs__repair_type=selected_repair).distinct()
#         return render(request, 'carservice/select_repair.html', {'services': services, 'selected_repair': selected_repair})
#     return render(request, 'carservice/select_repair.html', {'repair_types': repair_types})


#  Времено меняю 
# def select_repair(request):
#     form = ServiceSearchForm(request.GET)
#     repair_types = RepairType.objects.all()
#     if form.is_valid():
#         car_brand = form.cleaned_data.get('car_brand')
#         repair_type = form.cleaned_data.get('repair_type')
#         if car_brand:
#             services = AutoService.objects.filter(car_brands=car_brand)
#         else:
#             services = AutoService.objects.all()
#         if repair_type:
#             services = services.filter(repairs__repair_type=repair_type)
#     else:
#         services = AutoService.objects.all()
#     return render(request, 'carservice/select_repair.html', {'services': services, 'form': form, 'repair_types': repair_types})

def select_repair(request):
    form = ServiceSearchForm(request.GET)
    repair_types = RepairType.objects.all()
    services = AutoService.objects.all()
    if form.is_valid():
        car_brand = form.cleaned_data.get('car_brand')
        car_model = form.cleaned_data.get('car_model')
        repair_type = form.cleaned_data.get('repair_type')
        if car_brand:
            services = services.filter(car_brands=car_brand)
        if car_model:
            services = services.filter(car_models=car_model)
        if repair_type:
            services = services.filter(repairs=repair_type)
    return render(request, 'carservice/select_repair.html', {'services': services, 'form': form, 'repair_types': repair_types})


@login_required
def add_review(request, service_id):
    service = get_object_or_404(Service, id=service_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.service = service
            review.user = request.user
            review.save()
            return redirect('service_detail', service_id=service.id)
    else:
        form = ReviewForm()
    return render(request, 'carservice/add_review.html', {'form': form, 'service': service})




def signup_view(request):
  if request.method == 'POST':
    form = SignupForm(request.POST)
    if form.is_valid():
      user = form.save(commit=False)
      user.set_password(form.cleaned_data['password'])  # Хэшируем пароль
      user.save()
      return redirect('signin')
  else:
    form = SignupForm()
  return render(request, 'auth/signup.html', {'form': form})    


def signin(request):
  if request.method == "POST":
    username = request.POST.get("username")
    password = request.POST.get("password")
    
    # Аутентификация пользователя
    user = authenticate(request, username=username, password=password)
    if user is not None:
      login(request, user)  # Вход пользователя
      return redirect('service_list')  # Перенаправление после успешного входа
    else:
      # Ошибка входа
      return render(request, 'auth/signin.html', {'error': 'Неверный логин или пароль'})
  return render(request, 'auth/signin.html')  


def signout(request):
  # Выходим из системы
  logout(request)
  # Перенаправляем пользователя на страницу входа
  return redirect('signin')
