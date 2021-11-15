from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AbstractUser, PermissionsMixin

from django.utils.translation import ugettext_lazy as _
from django.db import models

from .managers import *

from django.utils import timezone

# 1
class Subject(models.Model):
    SUBJECT_CHOICES = (
        ("LECTURE", 'Лекция'),
        ("PRACTICE", 'Практика'),
    )

    name = models.CharField(_('Название'), max_length=100)
    type = models.CharField(_('Тип'), choices=SUBJECT_CHOICES, default="LECTURE", max_length=50)

    class Meta:
        verbose_name = _('Дисциплина')
        verbose_name_plural = _('Дисциплины')

# 2
class Group(models.Model):
    name = models.CharField('Название', max_length=100)

    class Meta:
        verbose_name = _('Группа')
        verbose_name_plural = _('Группы')

# 3
class Teacher(models.Model): 
    surname = models.CharField('Фамилия', max_length=50)
    name = models.CharField('Имя', max_length=50)
    lastname = models.CharField('Отчество', max_length=50)

    email = models.CharField('Почта', max_length=30)
    # mark_avg = models.FloatField('Средняя оценка')

    class Meta:
        verbose_name = _('Преподаватель')
        verbose_name_plural = _('Преподаватели')

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

# class Data(models.Model):
#     teachers = []
#     students = []
#     subjects = []

#     def __init__(self) -> None:
#         pass

# 4
class Criterion(models.Model):
    name = models.CharField('Содержание критерия', max_length=999)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Критерий'
        verbose_name_plural = 'Критерии'    
    
# 5
class Student(AbstractBaseUser, PermissionsMixin):
    # required reg and auth field
    email = models.EmailField(_('Email'), unique=True, max_length=30)

    # personal info
    surname = models.CharField(_('Фамилия'), max_length=50, default="Christ")
    name = models.CharField(_('Имя'), max_length=50, default="Jesus")
    lastname = models.CharField(_('Отчество'), max_length=50, null=True)

    # permissions
    is_staff = models.BooleanField(_('Права администратора'), default=False)
    is_active = models.BooleanField(_('Учётная запись активна'), default=False)
    is_superuser = models.BooleanField(_('Права суперпользователя'), default=False)

    date_registration = models.DateTimeField(_('Дата и время регистрации'), default=timezone.now)
    date_joined = models.DateTimeField(_('Дата и время последнего входа в систему'), default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = StudentManager()

    def __str__(self) -> str:
        return self.email

    
    class Meta:
        verbose_name = _('Студент')
        verbose_name_plural = _('Студенты')

# 6
class StudentGroup(models.Model):
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    group_id = models.ForeignKey(Group, on_delete=models.CASCADE)

    class Meta:
        verbose_name = _('Студент-Группа')
        verbose_name_plural = _('Студенты-Группы')

# 7
class SubjectGroup(models.Model):
    subject_id = models.ForeignKey(Subject, on_delete=models.CASCADE)
    group_id = models.ForeignKey(Group, on_delete=models.CASCADE)

    semester = models.IntegerField(_('semester'), default=1)

    class Meta:
        verbose_name = _('Дисциплина-Группа')
        verbose_name_plural = _('Дисциплины-Группы')

 # 8
class TeacherSubject(models.Model):
    teacher_id = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    subject_id = models.ForeignKey(Subject, on_delete=models.CASCADE)

    class Meta:
        verbose_name = _('Преподаватель-Дисциплина')
        verbose_name_plural = _('Преподаватели-Дисциплины')

# 9
class SubjectStudentCriterionMark(models.Model):
    criterion_id = models.ForeignKey(Criterion, on_delete=models.CASCADE)
    subject_id = models.ForeignKey(Subject, on_delete=models.CASCADE)
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)

    mark = models.FloatField(_('mark'))

    # objects = SubjectStudentCriterionMarkManager()

    class Meta:
        verbose_name = _('Дисциплина-Студент-Критерий-Оценка')
        verbose_name_plural = _('Дисциплины-Студенты-Критерии-Оценки')