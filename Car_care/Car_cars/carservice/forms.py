from django import forms
from .models import RepairType

class RepairTypeForm(forms.Form):
    repair_type = forms.ModelChoiceField(queryset=RepairType.objects.all(), label='Выберите вид ремонта')



# #  Создать форму для моделей автомобиля ( марка, модель, год ....) по аналогу практического проекта.
# #  для сервиса тоже форму  виды работа  электрика, кузовной и пр...
# #  в одну все


# #  подумать приколы  с картой.
 
# from django import forms
# from .models import AvtoService

# class AvtoServiseForm(forms.ModelForm):
#   class Meta:
#     model = AvtoService
#     fields = ['service', 'repair_type', 'price', 'due_date']
  
#     widgets = {
#       'service': forms.Select(attrs={
#         'class': 'form-select',
#         'id': 'floatingProjectSelect',
#         'aria-label': 'Выбор ',
#         'required': True
#         }),
#          'repair_type': forms.TextInput(attrs={
#         'class': 'form-control',
#         'id': 'floatingTitle',
#         'placeholder': 'Очень простая задача',
#         'required': True
#       }),
#       'price': forms.TextInput(attrs={
#         'class': 'form-control',
#         'id': 'floatingDescription',
#         'placeholder': 'Нужно сделать несколько пунктов...',
#         'required': True
#       }),
#       'due_date': forms.DateInput(attrs={
#         'class': 'form-control',
#         'id': 'floatingDueDate',
#         'type': 'date',
#         'required': True
#       }),
#     }



















