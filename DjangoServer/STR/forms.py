from django.contrib.auth import get_user_model
# from .models import Student
# from django.forms import ModelForm, TextInput, Textarea, PasswordInput
# from django.core.exceptions import ValidationError
# from django.forms.fields import CharField

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import *

# Subjects
class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        widgets = {
            'type': forms.Select
        }
        fields = '__all__'

# Students
class StudentCreationForm(UserCreationForm):

    class Meta:
        model = Student
        fields = ('email', 'surname', 'name', 'lastname')


class StudentChangeForm(UserChangeForm):

    class Meta:
        model = Student
        fields = ('email', 'surname', 'name', 'lastname')


class RegistrationForm(UserCreationForm):
    surname = forms.CharField(required=True, label='Фамилия', max_length=50)
    name = forms.CharField(required=True, label='Имя', max_length=50)
    lastname = forms.CharField(required=False, label='Отчество', max_length=50)

    email = forms.EmailField(required=True, label='Email', max_length=30)

    password1 = forms.CharField(required=True, label='Пароль', max_length=30, widget=forms.PasswordInput)
    password2 = forms.CharField(required=True, label='Повторите пароль', max_length=30, widget=forms.PasswordInput)

    error_messages = {
        'email_exists': 'Пользователь с таким Email уже существует!',
        'password_mismatch': 'Пароли не совпадают!',
        'error': 'Форма не валидна!',
    }

    class Meta:
        model = get_user_model()
        fields = (
            'surname',
            'name',
            'lastname',
            'email',
            'password1',
            'password2',
       )

    def clean_password(self):
        if self.data['password1'] != self.data['password2']:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return self.data['password1']

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if get_user_model().objects.filter(email=email).exists():
            raise forms.ValidationError(
                self.error_messages['email_exists'],
                code='email_exists',
            )
        return email

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)

        user.surname = self.cleaned_data['surname']
        user.name = self.cleaned_data['name']
        user.lastname = self.cleaned_data['lastname']

        user.email = self.cleaned_data['email']
        
        user.password1 = self.cleaned_data['password1']
        user.password2 = self.cleaned_data['password2']

        if commit:
            user.save()
        return user


# class TicketForm(forms.ModelForm):
#     class Meta:
#         model = Ticket
#         fields = ["name", "description"]
#         widgets = {
#             "name": forms.TextInput(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Введите имя'
#             }),
#             "description": forms.Textarea(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Введите описание учебного предмета'
#             }),
#         }
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