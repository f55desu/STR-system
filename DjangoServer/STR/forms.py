from .models import Ticket
# from .models import Student
from django.forms import ModelForm, TextInput, Textarea, PasswordInput
from django.core.exceptions import ValidationError
from django.forms.fields import CharField
import js2py

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
# <!-- <h1>Регистрация</h1>
#     <form method="post">
#         {% csrf_token %}
#         {{ form.name }}<br>
#         {{ form.surname }}<br>
#         {{ form.lastname }}<br>
#         {{ form.login }}<br>
#         {{ form.password }}<br>
#         <button type="submit" class="btn btn-success">Зарегистрироваться</button>
#         <span>{{ error }}</span>
#     </form> -->

# class LoginForm(ModelForm):
#     login = CharField()
#     password = CharField(widget=PasswordInput)

#     class Meta:
#         model = Student
#         fields = ["login", "password"]
#         widgets = {
#             "login": TextInput(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Логин'
#             }),
#             "password": TextInput(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Пароль'
#             }),
#         }

# class RegistrationForm(ModelForm):
#     password = CharField(label='Пароль', widget=PasswordInput)
#     password2 = CharField(label='Повторите пароль', widget=PasswordInput)

#     class Meta:
#         model = Student
#         fields = ["surname", "name", "lastname", "login", "password"]
#         # widgets = {
#         #     "surname": TextInput(attrs={
#         #         'class': 'form-control',
#         #         'placeholder': 'Введите фамилию'
#         #     }),
#         #     "name": TextInput(attrs={
#         #         'class': 'form-control',
#         #         'placeholder': 'Введите имя'
#         #     }),
#         #     "lastname": TextInput(attrs={
#         #         'class': 'form-control',
#         #         'placeholder': 'Введите отчество'
#         #     }),
#         #     "login": TextInput(attrs={
#         #         'class': 'form-control',
#         #         'placeholder': 'Введите логин'
#         #     }),
#         #     "password": TextInput(attrs={
#         #         'class': 'form-control',
#         #         'placeholder': 'Введите пароль'
#         #     }),
#         #     "password2": TextInput(attrs={
#         #         'class': 'form-control',
#         #         'placeholder': 'Повторите пароль'
#         #     }),
#         # }

#     def clean_password2(self):
#         cd = self.cleaned_data
#         if cd['password'] != cd['password2']:
#             wrongPass = "console.log('Пароли не совпадают!')"
#             js2py.eval_js(wrongPass)
#         return cd['password2']        

#         # вывод ошибки при повторном вводе пароля
#         #if widgets[5] != widgets[4]:
#            # pass   