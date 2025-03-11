from django.shortcuts import render, redirect
from .models import Request
from .forms import RequestForm

def create_request(request):
    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('request_list')
    else:
        form = RequestForm()
    return render(request, 'requests/create_request.html', {'form': form})

def request_list(request):
    requests = Request.objects.all().order_by('-submitted_at')  # Сортировка по дате подачи заявки
    return render(request, 'requests/request_list.html', {'requests': requests})


# from django.shortcuts import render, redirect
# from .models import Request  # Предполагается, что у вас есть модель Request
# from .forms import RequestForm


# def create_request(request):

#     if request.method == 'POST':
#        form = RequestForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('request_list')
#     else:
#         form = RequestForm()
#     return render(request, 'requests/create_request.html', {'form': form})


# def request_list(request):
#     requests = Request.objects.all()  # Получение всех заявок
#     return render(request, 'requests/list.html', {'requests': requests})  # Шаблон для списка

# # Create your views here.
