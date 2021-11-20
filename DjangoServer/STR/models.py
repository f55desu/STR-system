from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin

from django.utils.translation import ugettext_lazy as _
from django.db import models

from .managers import *

from django.utils import timezone

# 1
class Subject(models.Model):
    SUBJECT_CHOICES = (
        ("Лекция", 'Лекция'),
        ("Практика", 'Практика'),
    )

    name = models.CharField(_('Название'), max_length=100)
    type = models.CharField(_('Тип'), default="Лекция", choices=SUBJECT_CHOICES, max_length=50)

    # def __str__(self) -> str:
    #     return f"{self.name} ({self.get_type_display()})"

    def __str__(self) -> str:
        return f"{self.name} ({self.type})"

    class Meta:
        verbose_name = _('Дисциплина')
        verbose_name_plural = _('Дисциплины')

# 2
class Group(models.Model):
    name = models.CharField('Название', unique=True, max_length=100)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = _('Группа')
        verbose_name_plural = _('Группы')

# 3
class Teacher(models.Model): 
    surname = models.CharField('Фамилия', max_length=50)
    name = models.CharField('Имя', max_length=50)
    lastname = models.CharField('Отчество', blank=True, max_length=50)

    email = models.CharField('Почта', unique=True, max_length=30)
    # mark_avg = models.FloatField('Средняя оценка')

    def __str__(self) -> str:
        return f"{self.surname} {self.name} {self.lastname} ({self.email})"

    class Meta:
        verbose_name = _('Преподаватель')
        verbose_name_plural = _('Преподаватели')

# 4
class Criterion(models.Model):
    name = models.CharField('Содержание критерия', unique=True, max_length=999)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Критерий'
        verbose_name_plural = 'Критерии'    
    
# 5
class Student(AbstractBaseUser, PermissionsMixin):
    # required reg and auth field
    email = models.EmailField(_('Email'), unique=True)

    # personal info
    surname = models.CharField(_('Фамилия'), default="Christ", max_length=50)
    name = models.CharField(_('Имя'), default="Jesus", max_length=50)
    lastname = models.CharField(_('Отчество'), blank=True, max_length=50)

    group_name = models.ForeignKey('Group', to_field='name', db_column='group_name', null=True, default=None, blank=True, on_delete=models.PROTECT)

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
        return f"{self.surname} {self.name} {self.lastname} ({self.group_name})"
    
    class Meta:
        verbose_name = _('Студент')
        verbose_name_plural = _('Студенты')

# 6
class Subject_Group(models.Model):
    subject_id = models.ForeignKey('Subject', on_delete=models.PROTECT)
    group_id = models.ForeignKey('Group', to_field='name', on_delete=models.PROTECT)

    semester = models.PositiveSmallIntegerField(_('Семестр'), default=1)

    def __str__(self) -> str:
        return f"Семестр {self.semester}: {self.group_id} / {self.subject_id}"

    class Meta:
        verbose_name = _('Дисциплина_Группа')
        verbose_name_plural = _('Дисциплины_Группы')

# 7
class Teacher_Subject(models.Model):
    teacher_id = models.ForeignKey('Teacher', on_delete=models.PROTECT)
    subject_id = models.ForeignKey('Subject', on_delete=models.PROTECT)

    def __str__(self) -> str:
        return f"{self.teacher_id} / {self.subject_id}"

    class Meta:
        verbose_name = _('Преподаватель_Дисциплина')
        verbose_name_plural = _('Преподаватели_Дисциплины')

# 8
class Grade(models.Model):
    teacher_subject_id = models.ForeignKey('Teacher_Subject', on_delete=models.PROTECT)
    student_id = models.ForeignKey('Student', on_delete=models.PROTECT)
    criterion_name = models.ForeignKey('Criterion', to_field='name', db_column='criterion_name', on_delete=models.PROTECT)    

    grade = models.PositiveSmallIntegerField(_('Оценка'), null=True, default=0)

    # objects = SubjectStudentCriterionMarkManager()
    def __str__(self) -> str:
        return f"Студент: {self.student_id} / Преподаватель: {self.teacher_subject_id} / Критерий: {self.criterion_name} / Оценка: ({self.grade})"

    class Meta:
        verbose_name = _('Оценка')
        verbose_name_plural = _('Оценки')



