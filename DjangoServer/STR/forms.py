# from typing import List, Tuple
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms

from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import *


class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        widgets = {
            'type': forms.Select
        }
        fields = '__all__'


class StudentCreationForm(UserCreationForm):

    class Meta:
        model = Student
        fields = ('email', 'surname', 'name', 'lastname', 'password', 'group')


class StudentChangeForm(UserChangeForm):

    class Meta:
        model = Student
        fields = ('email', 'surname', 'name', 'lastname', 'password', 'group')

# def _all_groups() -> List[Tuple[str, str]]:
#     from django.db import connection
#     with connection.cursor() as cursor:
#         cursor.execute("SELECT name id FROM STR_group order by id")
#         return [(row[0], row[0]) for row in cursor.fetchall()]


class RegistrationForm(UserCreationForm):

    # def __init__(self, *args, **kwargs) -> None:
    #     super().__init__(*args, **kwargs)
    #     self.fields['group'].choices = _all_groups()

    surname = forms.CharField(required=True, label='Фамилия', max_length=50)
    name = forms.CharField(required=True, label='Имя', max_length=50)
    lastname = forms.CharField(required=False, label='Отчество', max_length=50)

    email = forms.EmailField(required=True, label='Email', max_length=30)

    # group = forms.ChoiceField(required=True, label='Группа', choices=[])
    group = forms.ModelChoiceField(required=True, label='Группа', queryset=Group.objects.all().order_by('name'), initial=0)

    # groupNumber = forms.ChoiceField(required=True, label='Группа', choices=GROUP_NUMBERS)

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
            'group',
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

        user.group = self.cleaned_data['group']

        user.password1 = self.cleaned_data['password1']
        user.password2 = self.cleaned_data['password2']

        if commit:
            user.save()
        return user