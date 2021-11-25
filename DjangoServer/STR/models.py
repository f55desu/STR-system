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

    name = models.CharField(_('Название'), max_length=320)
    type = models.CharField(_('Тип'), default="Лекция", choices=SUBJECT_CHOICES, max_length=50)

    # def __str__(self) -> str:
    #     return f"{self.name} ({self.get_type_display()})"

    def __str__(self) -> str:
        return f"{self.name} ({self.type})"

    class Meta:
        verbose_name = _('Дисциплина')
        verbose_name_plural = _('Дисциплины')
        unique_together = ('name', 'type', )

# 2
class Group(models.Model):
    name = models.CharField('Название', unique=True, max_length=320)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = _('Группа')
        verbose_name_plural = _('Группы')

# 3
class Teacher(models.Model): 
    surname = models.CharField('Фамилия', max_length=320)
    name = models.CharField('Имя', max_length=320)
    lastname = models.CharField('Отчество', blank=True, null=True, default=None, max_length=320)

    email = models.CharField('Почта', unique=True, max_length=320)
    # mark_avg = models.FloatField('Средняя оценка')

    def __str__(self) -> str:
        return f"{self.surname} {self.name} {self.lastname} ({self.email})"

    class Meta:
        verbose_name = _('Преподаватель')
        verbose_name_plural = _('Преподаватели')

# 4
class Criterion(models.Model):
    name = models.CharField('Содержание критерия', unique=True, max_length=320)

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
    surname = models.CharField(_('Фамилия'), default="Christ", max_length=320)
    name = models.CharField(_('Имя'), default="Jesus", max_length=320)
    lastname = models.CharField(_('Отчество'), blank=True, null=True, default=None, max_length=320)

    group = models.ForeignKey('Group', verbose_name=_('Группа'), blank=True, null=True, default=None, on_delete=models.PROTECT)

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
        return f"{self.surname} {self.name} {self.lastname} ({self.group})"

    def get_full_name(self):
        if self.lastname:
            return f"{self.surname} {self.name} {self.lastname}"
        return f"{self.surname} {self.name}"
    
    class Meta:
        verbose_name = _('Студент')
        verbose_name_plural = _('Студенты')

# 6
class Subject_Group(models.Model):
    subject = models.ForeignKey('Subject', verbose_name=_('Дисциплина'), on_delete=models.PROTECT)
    group = models.ForeignKey('Group', verbose_name=_('Группа'), on_delete=models.PROTECT)

    semester = models.PositiveSmallIntegerField(_('Семестр'), default=1)

    def __str__(self) -> str:
        return f"Семестр {self.semester}: {self.group} / {self.subject}"

    class Meta:
        verbose_name = _('Дисциплина_Группа')
        verbose_name_plural = _('Дисциплины_Группы')
        unique_together = ('subject', 'group', 'semester', )

# 7
class Teacher_Subject(models.Model):
    teacher = models.ForeignKey('Teacher', verbose_name=_('Преподаватель'), on_delete=models.PROTECT)
    subject = models.ForeignKey('Subject', verbose_name=_('Дисциплина'), on_delete=models.PROTECT)

    def __str__(self) -> str:
        return f"{self.teacher} / {self.subject}"

    class Meta:
        verbose_name = _('Преподаватель_Дисциплина')
        verbose_name_plural = _('Преподаватели_Дисциплины')
        unique_together = ('teacher', 'subject', )

# 8
class Grade(models.Model):
    teacher_subject = models.ForeignKey('Teacher_Subject', verbose_name=_('Преподаватель_Дисциплина'), on_delete=models.PROTECT)
    student = models.ForeignKey('Student', verbose_name=_('Студент'), on_delete=models.PROTECT)
    criterion = models.ForeignKey('Criterion', verbose_name=_('Критерий'), on_delete=models.PROTECT)    

    grade = models.PositiveSmallIntegerField(_('Оценка'), default=0)

    # objects = SubjectStudentCriterionMarkManager()
    def __str__(self) -> str:
        return f"Студент: {self.student} / Преподаватель: {self.teacher_subject} / Критерий: {self.criterion} / Оценка: ({self.grade})"

    class Meta:
        verbose_name = _('Оценка')
        verbose_name_plural = _('Оценки')
        unique_together = ('teacher_subject', 'student', 'criterion', 'grade', )



