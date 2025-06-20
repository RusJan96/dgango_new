from django import forms
from .models import RepairType, CarBrand, CarModel, AutoService, Review, ServiceRepair, Review
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

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
# class SignupForm(forms.ModelForm):

# дип сик 
class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']
        
        labels = {
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'username': 'Имя пользователя',
            'email': 'Почта',
            'password1': 'Пароль',
            'password2': 'Подтверждение пароля'
        }
        
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите ваше имя',
                'autofocus': True  # Автофокус на это поле при загрузке
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите вашу фамилию'
            }),
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Придумайте логин'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'example@mail.com'
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Настройка полей паролей
        self.fields['password1'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Не менее 8 символов'
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Повторите пароль'
        })
        
        # Убираем ВСЕ вспомогательные тексты
        for field in self.fields.values():
            field.help_text = None
            field.widget.attrs['aria-describedby'] = ''

# class SignupForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password1', 'password2']
        
#         labels = {
#             'username': 'Логин',
#             'email': 'Почта',
#             'password1': 'Пароль',
#             'password2': 'Подтверждение пароля'
#         }
        
#         widgets = {
#             'username': forms.TextInput(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Введите логин'
#             }),
#             'email': forms.EmailInput(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Введите почту'
#             }),
#         }

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         # Настройка полей паролей
#         self.fields['password1'].widget.attrs.update({
#             'class': 'form-control',
#             'placeholder': 'Введите пароль'
#         })
#         self.fields['password2'].widget.attrs.update({
#             'class': 'form-control',
#             'placeholder': 'Подтвердите пароль'
#         })
        
#         # Убираем ВСЕ вспомогательные тексты
#         for field in self.fields.values():
#             field.help_text = None
#             field.widget.attrs['aria-describedby'] = ''  # Убираем связь с подсказками

# class SignupForm(UserCreationForm):
#   confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
#     'class': 'form-control',
#     'id': 'floatingPasswordConfirm',
#     'placeholder': 'Подтверждение пароля',
#     'required': True
#   }))

#   class Meta:
#     model = User
#     fields = ['first_name', 'last_name', 'username', 'email', 'password']

#     widgets = {
#       'first_name': forms.TextInput(attrs={
#         'class': 'form-control',
#         'id': 'floatingTitle',
#         'placeholder': 'Очень простая задача',
#         'required': True
#       }),
#       'last_name': forms.TextInput(attrs={
#         'class': 'form-control',
#         'id': 'floatingLastname',
#         'aria-label': 'Фамилия',
#         'placeholder': 'Очень простая задача',
#         'required': True
#       }),
#       'username': forms.TextInput(attrs={
#         'class': 'form-control',
#         'id': 'floatingUsername',
#         'placeholder': 'Логин пользователя',
#         'aria-label': 'Логин пользователя',
#         'required': True
#       }),
#       'email': forms.EmailInput(attrs={
#         'class': 'form-control',
#         'id': 'floatingEmail',
#         'placeholder': 'Почта',
#         'required': True
#       }),
#       'password': forms.PasswordInput(attrs={
#         'class': 'form-control',
#         'id': 'floatingPassword',
#         'placeholder': 'Пароль',
#         'required': True
#       }),
#     }

#   def clean(self):
#     cleaned_data = super().clean()
#     password = cleaned_data.get('password')
#     confirm_password = cleaned_data.get('confirm_password')
#     if password != confirm_password:
#       raise forms.ValidationError('Пароли не совпадают!')
#     return cleaned_data




# Ии предлогает такую форму 
# class SignupForm(UserCreationForm):
#     email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
#     first_name = forms.CharField(required=True, max_length=30, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Имя'}))
#     last_name = forms.CharField(required=True, max_length=30, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Фамилия'}))

#     class Meta:
#         model = User
#         fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
#         widgets = {
#             'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Имя пользователя'}),
#             'password1': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Пароль'}),
#             'password2': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Подтверждение пароля'}),
#         }
#     def clean(self):
#     cleaned_data = super().clean()
#     password = cleaned_data.get('password')
#     confirm_password = cleaned_data.get('confirm_password')
#     if password != confirm_password:
#       raise forms.ValidationError('Пароли не совпадают!')
#     return cleaned_data



# class SignupForm(UserCreationForm):
#     email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
#     first_name = forms.CharField(required=True, max_length=30, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Имя'}))
#     last_name = forms.CharField(required=True, max_length=30, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Фамилия'}))

#     class Meta:
#         model = User  # Правильный импорт
#         fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
#         widgets = {
#             'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Имя пользователя'}),
#             'password1': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Пароль'}),
#             'password2': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Подтверждение пароля'}),
#         }










