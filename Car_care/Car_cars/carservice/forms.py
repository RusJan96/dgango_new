from django import forms
from .models import RepairType, CarBrand, CarModel, AutoService, Review, ServiceRepair, Review

class ServiceRepairForm(forms.ModelForm):
    class Meta:
        model = ServiceRepair
        fields = ['repair_type', 'price', 'duration']
        widgets = {
            'repair_type': forms.Select(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'duration': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class RepairTypeForm(forms.Form):
    repair_type = forms.ModelChoiceField(queryset=RepairType.objects.all(), label='Выберите вид ремонта')


class ServiceSearchForm(forms.Form):
    car_brand = forms.ModelChoiceField(
        queryset=CarBrand.objects.all(),
        label='Марка автомобиля',
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    car_model = forms.ModelChoiceField(
        queryset=CarModel.objects.none(),  # Инициализируем пустым queryset
        label='Модель автомобиля',
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    repair_type = forms.ModelChoiceField(
        queryset=RepairType.objects.all(),
        label='Вид ремонта',
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    def __init__(self, *args, **kwargs):
        super(ServiceSearchForm, self).__init__(*args, **kwargs)
        if 'car_brand' in self.data:
            try:
                car_brand_id = int(self.data.get('car_brand'))
                self.fields['car_model'].queryset = CarModel.objects.filter(brand_id=car_brand_id).order_by('name')
            except (ValueError, TypeError):
                self.fields['car_model'].queryset = CarModel.objects.none() 
        elif self.instance.pk:
            self.fields['car_model'].queryset = self.instance.car_brand.models.order_by('name')

            
class ServiceSearchForm(forms.Form):
    car_brand = forms.ModelChoiceField(queryset=CarBrand.objects.all(), label='Марка автомобиля', required=False)
    # car_model = forms.ModelChoiceField(queryset=CarModel.objects.all(), label='Модель  автомобиля', required=False)
    repair_type = forms.ModelChoiceField(queryset=RepairType.objects.all(), label='Вид ремонта', required=False)

    def __init__(self, *args, **kwargs):
        super(ServiceSearchForm, self).__init__(*args, **kwargs)
        self.fields['car_brand'].empty_label = "Все марки"
        # self.fields['car_model'].empty_label = "Все модели"
        self.fields['repair_type'].empty_label = "Все виды ремонта"


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['comment', 'rating']
        widgets = {
            'comment': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Ваш отзыв'}),
            'rating': forms.NumberInput(attrs={'class': 'form-control', 'min': 1, 'max': 5, 'placeholder': 'Оценка'}),
        }


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



















