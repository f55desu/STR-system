from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin

from django.utils.translation import gettext_lazy as _
from django.db import models

from .managers import *

# from django.utils import timezone


# STR-module models:
# 1 
class User(AbstractBaseUser, PermissionsMixin):
    # required reg and auth field
    email = models.EmailField(_('Email'), unique=True)

    # personal info
    surname = models.CharField(_('Фамилия'), default="Christ", max_length=320)
    name = models.CharField(_('Имя'), default="Jesus", max_length=320)
    lastname = models.CharField(_('Отчество'), blank=True, null=True, default=None, max_length=320)

    # permissions
    is_superuser = models.BooleanField(_('Права суперпользователя'), default=False)
    is_staff = models.BooleanField(_('Права администратора'), default=False)
    is_active = models.BooleanField(_('Учётная запись активна'), default=False)

    is_teacher = models.BooleanField(_('Преподаватель'), default=False)
    is_student = models.BooleanField(_('Студент'), default=False)

    date_joined = models.DateTimeField(_('Регистрация'), auto_now_add=True)
    date_modified = models.DateTimeField(_('Последнее изменение'), auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self) -> str:
        return f"{self.surname} {self.name} {self.lastname} ({self.email})"

    def get_full_name(self):
        if self.lastname:
            return f"{self.surname} {self.name} {self.lastname}"
        return f"{self.surname} {self.name}"
    
    class Meta:
        verbose_name = _('Пользователь')
        verbose_name_plural = _('Пользователи')


# 2
class Subject(models.Model):
    name = models.CharField(_('Название'), max_length=320)

    # def __str__(self) -> str:
    #     return f"{self.name} ({self.get_type_display()})"

    def __str__(self) -> str:
        return f"{self.name}"

    class Meta:
        verbose_name = _('Дисциплина')
        verbose_name_plural = _('Дисциплины')
        unique_together = ('name', )


# 3
class Group(models.Model):
    EDUFORM_CHOICES = (
        ("Очная", 'Очная'),
        ("Очно-заочная", 'Очно-заочная'),
        ("Заочная", 'Заочная'),
    )

    name = models.CharField('Название', unique=True, max_length=320)

    education_form = models.CharField('Форма обучения', choices=EDUFORM_CHOICES, max_length=170)
    
    def __str__(self) -> str:
        return f"{self.name}"

    class Meta:
        verbose_name = _('Группа')
        verbose_name_plural = _('Группы')


# 4
class Teacher(models.Model): 
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self) -> str:
        return f"{self.user.surname} {self.user.name} {self.user.lastname} ({self.user.email})"

    def get_FIO(self):
        if self.user.lastname:
            return f"{self.user.surname} {self.user.name[0]}. {self.user.lastname[0]}."
        return f"{self.user.surname} {self.user.name[0]}."

    class Meta:
        verbose_name = _('Преподаватель')
        verbose_name_plural = _('Преподаватели')


# 5
class Criterion(models.Model):
    name = models.CharField('Содержание критерия', unique=True, max_length=320)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Критерий'
        verbose_name_plural = 'Критерии'    
    

# 6
class Student(models.Model):
    SUBGROUP_CHOICES = (
        (1, 1),
        (2, 2),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    group = models.ForeignKey('Group', verbose_name=_('Группа'), blank=True, null=True, default=None, on_delete=models.PROTECT)
    subgroup_number = models.SmallIntegerField(_('Подгруппа'), default=1, choices=SUBGROUP_CHOICES)

    def __str__(self) -> str:
        return f"{self.user.surname} {self.user.name} {self.user.lastname} ({self.group})"

    def get_full_name(self):
        if self.user.lastname:
            return f"{self.user.surname} {self.user.name} {self.user.lastname}"
        return f"{self.user.surname} {self.user.name}"
    
    class Meta:
        verbose_name = _('Студент')
        verbose_name_plural = _('Студенты')


# 7
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


# 8
class Teacher_Subject(models.Model):
    teacher = models.ForeignKey('Teacher', verbose_name=_('Преподаватель'), on_delete=models.PROTECT)
    subject = models.ForeignKey('Subject', verbose_name=_('Дисциплина'), on_delete=models.PROTECT)

    def __str__(self) -> str:
        return f"{self.teacher} / {self.subject}"

    class Meta:
        verbose_name = _('Преподаватель_Дисциплина')
        verbose_name_plural = _('Преподаватели_Дисциплины')
        unique_together = ('teacher', 'subject', )


# 9
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


# Schedule-module models:
# 10
class Campus(models.Model):
    campus_name = models.CharField('Название корпуса', max_length=75, unique=True)
    address = models.CharField('Адрес корпуса', max_length=175)

    def __str__(self) -> str:
        return f"{self.campus_name[8]}"

    class Meta:
        verbose_name = _('Корпус')
        verbose_name_plural = _('Корпуса')


# 11
class Audience(models.Model):
    AUDIENCE_CHOICES = (
        ("Лекционная", 'Лекционная'),
        ("Лабораторная", 'Лабораторная')
    )

    audience_number = models.IntegerField('Номер аудитории', unique=True)
    campus = models.ForeignKey(Campus, verbose_name = 'Корпус', on_delete=models.CASCADE)
    audience_type = models.CharField('Тип аудитории', default="", choices=AUDIENCE_CHOICES, max_length=70)
    capacity = models.IntegerField('Вместимость')

    def __str__(self) -> str:
         return f"{self.audience_number}/{self.campus}"
        # if self.capacity > 0:
        #     if self.capacity == 1:
        #         return f"{self.audience_type}, {self.campus}/{self.audience_number} на {self.capacity} человека"
        #     else:
        #         return f"{self.audience_type}, {self.campus}/{self.audience_number} на {self.capacity} человек"

    class Meta:
        verbose_name = _('Аудитория')
        verbose_name_plural = _('Аудитории')


# 12
class Schedule(models.Model):
    TIME_CHOICES = (
        ("C 8:00 до 9:30", 'C 8:00 до 9:30'),
        ("С 9:45 до 11:15", 'С 9:45 до 11:15'),
        ("С 11:30 до 13:15", 'С 11:30 до 13:15'),
        ("С 13:30 до 15:00", 'С 13:30 до 15:00'),
        ("С 15:15 до 16:45", 'С 15:15 до 16:45'),
        ("С 17:00 до 18:30", 'С 17:00 до 18:30'),
    )
    WEEKDAY_CHOICES = (
        ("Понедельник", 'Понедельник'),
        ("Вторник", 'Вторник'),
        ("Среда", 'Среда'),
        ("Четверг", 'Четверг'),
        ("Пятница", 'Пятница'),
        ("Суббота", 'Суббота'),
    )
    EVEN_CHOICES = (
        ("Числитель", 'Числитель'),
        ("Знаменатель", 'Знаменатель'),
    )
    SUBGROUP_CHOICES = (
        (1, 1),
        (2, 2),
    )
    SUBJECT_CHOICES = (
        ("Лекция", 'Лекция'),
        ("Практика", 'Практика'),
    )

    teacher = models.ForeignKey(Teacher, verbose_name = 'Преподаватель', on_delete=models.PROTECT)

    subject = models.ForeignKey(Subject, verbose_name = 'Дисциплина',on_delete=models.PROTECT)
    subject_type = models.CharField(_('Тип занятия'), default="Лекция", choices=SUBJECT_CHOICES, max_length=50)

    group = models.ForeignKey(Group, verbose_name = 'Группа', on_delete=models.PROTECT)
    subgroup_number = models.SmallIntegerField(_('Подгруппа'), default=1, choices=SUBGROUP_CHOICES)

    semester_year = models.CharField('Семестр', max_length=70)
    even_week = models.CharField('Четность', default="", choices=EVEN_CHOICES, max_length=20)
    weekday = models.CharField('День недели', default="", choices=WEEKDAY_CHOICES, max_length=20)
    time_range = models.CharField('Время', default="", choices=TIME_CHOICES, max_length=40)

    audience = models.ForeignKey(Audience, verbose_name = 'Аудитория', on_delete=models.PROTECT)

    def __str__(self) -> str:
        return f"[{self.subject}], [{self.audience}], [{self.group}], [{self.time_range}], [{self.weekday}], [{self.even_week}], [{self.subgroup_number}], [{self.teacher}], [{self.semester_year}]"

    class Meta:
        verbose_name = _('Расписание')
        verbose_name_plural = _('Расписания')


# Attendance-module models:
# 13
class Attendance(models.Model):
    attended = models.BooleanField()

    schedule = models.ForeignKey(Schedule, on_delete=models.PROTECT)
    student = models.ForeignKey(Student, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return f'{self.schedule.teacher} {self.schedule.subject.name} {self.schedule.group} {self.schedule.subgroup_number} {self.student}'

    class Meta:
        verbose_name = 'Посещаемость'
        verbose_name_plural = _('Посещаемость')