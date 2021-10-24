from .models import Ticket
from .models import Student
from django.forms import ModelForm, TextInput, Textarea

class TicketForm(ModelForm):
    class Meta:
        model = Ticket
        fields = ["name", "description"]
        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите имя'
            }),
            "description": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите описание учебного предмета'
            }),
        }

class RegistrationForm(ModelForm):
    class Meta:
        model = Student
        fields = ["surname", "name", "lastname", "login", "password"]
        widgets = {
            "surname": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите фамилию'
            }),
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите имя'
            }),
            "lastname": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите отчество'
            }),
             "login": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите логин'
            }),
            "password": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите пароль'
            }),
        }

        # вывод ошибки при повторном вводе пароля
        #if widgets[5] != widgets[4]:
           # pass   