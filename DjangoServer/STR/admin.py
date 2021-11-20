from django.contrib.auth.admin import UserAdmin
from django.contrib import admin

from django.forms import *

from .forms import *
from .models import *

import django.contrib.auth.models as mod

class Student_Admin(UserAdmin):
    add_form = StudentCreationForm
    form = StudentChangeForm
    model = Student

    # список юзеров в админке
    list_display = ('email', 'surname', 'name', 'lastname', 'group_name', 'is_staff', 'is_active', 'is_superuser', )

    # фильтр в админке
    list_filter = ('is_staff', 'is_active', 'is_superuser', )

    # просмотр и изменение полей
    fieldsets = (
        (None, {'fields': ('email', 'surname', 'name', 'lastname', 'group_name', 'password', 'date_joined', 'date_registration', )}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser', )}),
    )

    # поля при добавлении в админке
    add_fieldsets = (
        (None, {
            'classes': ('wide', ),
            'fields': ('email', 'surname', 'name', 'lastname', 'group_name', 'password1', 'password2', 'is_staff', 'is_active', 'is_superuser', )}
        ),
    )

    # поиск по полям
    search_fields = ('email', 'surname', 'name', 'lastname', 'group_name__name', )

    # сортировка списка по полям
    ordering = ('email', 'surname', 'name', 'lastname', 'group_name', )


class Teacher_Admin(admin.ModelAdmin):
    model = Teacher
    list_display = ('email', 'surname', 'name', 'lastname', )
    search_fields = ('email', 'surname', 'name', 'lastname', )
    ordering = ('email', 'surname', 'name', 'lastname', )


class Criterion_Admin(admin.ModelAdmin):
    model = Criterion
    list_display = ('name', )
    search_fields = ('name', )
    ordering = ('name', )


class Group_Admin(admin.ModelAdmin):
    model = Group
    list_display = ('name', )
    search_fields = ('name', )
    ordering = ('name', )


class Subject_Admin(admin.ModelAdmin):
    model = Subject
    form = SubjectForm
    list_display = ('name', 'type', )
    search_fields = ('name', 'type', )
    ordering = ('name', 'type', )


class Subject_Group_Admin(admin.ModelAdmin):
    model = Subject_Group
    list_display = ('id', 'group_id', 'semester', 'subject_id', )
    search_fields = ('semester', 'group_id__name', 'subject_id__type', 'subject_id__name', 'id', )
    ordering = ('id', 'group_id', 'semester', 'subject_id', )


class Teacher_Subject_Admin(admin.ModelAdmin):
    model = Teacher_Subject
    list_display = ('id', 'teacher_id', 'subject_id', )
    search_fields = ('teacher_id__email', 'teacher_id__surname', 'teacher_id__name', 'teacher_id__lastname', 'subject_id__type', 'subject_id__name', 'id', )
    ordering = ('id', 'teacher_id', 'subject_id', )


class Grade_Admin(admin.ModelAdmin):
    model = Grade
    list_display = ('id', 'student_id', 'teacher_subject_id', 'criterion_name', 'grade', )
    search_fields = ('student_id__email', 'student_id__surname', 'student_id__name', 'student_id__lastname', 'criterion_name__name', 'teacher_subject_id__subject_id__type', 'teacher_subject_id__subject_id__name', 'teacher_subject_id__teacher_id__email', 'teacher_subject_id__teacher_id__surname', 'teacher_subject_id__teacher_id__name', 'teacher_subject_id__teacher_id__lastname', 'grade', 'id', )
    ordering = ('id', 'student_id', 'teacher_subject_id', 'criterion_name', 'grade', )


admin.site.unregister(mod.Group)

admin.site.register(Student, Student_Admin)
admin.site.register(Teacher, Teacher_Admin)
admin.site.register(Criterion, Criterion_Admin)
admin.site.register(Group, Group_Admin)
admin.site.register(Subject, Subject_Admin)

admin.site.register(Subject_Group, Subject_Group_Admin)
admin.site.register(Teacher_Subject, Teacher_Subject_Admin)
admin.site.register(Grade, Grade_Admin)