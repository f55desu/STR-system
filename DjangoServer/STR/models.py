from django.db import models

# Create your models here.
class Subject(models.Model):
    name = models.CharField('Название', max_length=100)

class Person(models.Model):
    surname = models.CharField('Фамилия', max_length=50)
    name = models.CharField('Имя', max_length=50)
    lastname = models.CharField('Отчество', max_length=50)

class Student(Person):
    login = models.CharField('Логин', max_length=30)
    password = models.CharField('Пароль', max_length=16)
    marks = [[1,2,3],[4,5,6]]

class Teacher(Person): 
    email = models.CharField('Почта', max_length=30)
    mark_avg = models.FloatField('Средняя оценка')

class Mark(models.Model):
    ticket_id = models.IntegerField('Номер вопроса')
    mark = models.IntegerField('Оценка')

# class SingletonDataMeta(models.Model):
#     """
#     The Singleton class can be implemented in different ways in Python. Some
#     possible methods include: base class, decorator, metaclass. We will use the
#     metaclass because it is best suited for this purpose.
#     """

#     _instances = {}

#     def __call__(cls, *args, **kwargs):
#         """
#         Possible changes to the value of the `__init__` argument do not affect
#         the returned instance.
#         """
#         if cls not in cls._instances:
#             instance = super().__call__(*args, **kwargs)
#             cls._instances[cls] = instance
#         return cls._instances[cls]

class Data(models.Model):
    teachers = []
    students = []
    subjects = []

    def __init__(self) -> None:
        pass

# переделать
class Ticket(models.Model):
    name = models.CharField('Название', max_length=50)
    description = models.TextField('Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'    