from django.urls import path
from . import views

urlpatterns = [
    path('', views.service_list, name='service_list'),
    path('select_repair/', views.select_repair, name='select_repair'),
    path('service/<int:pk>/', views.service_detail, name='service_detail'),
]