from django.contrib.auth.admin import UserAdmin
from django.contrib import admin

from django.forms import *

from .forms import *
from .models import *

import django.contrib.auth.models as mod

class User_Admin(UserAdmin):
    add_form = MyUserCreationForm
    form = MyUserChangeForm
    model = User

    readonly_fields = ('date_joined', 'date_modified', 'last_login', )

    # список юзеров в админке
    list_display = ('email', 'surname', 'name', 'lastname', 'is_superuser', 'is_staff', 'is_active', 'is_teacher', 'is_student', )

    # фильтр в админке
    list_filter = ('is_superuser', 'is_staff', 'is_active', 'is_teacher', 'is_student', )

    # просмотр и изменение полей
    fieldsets = (
        (None, {'fields': ('email', 'surname', 'name', 'lastname', 'password', 'date_joined', 'date_modified', 'last_login', )}),
        ('Permissions', {'fields': ('is_superuser', 'is_staff', 'is_active', 'is_teacher', 'is_student', )}),
    )

    # поля при добавлении в админке
    add_fieldsets = (
        (None, {
            'classes': ('wide', ),
            'fields': ('email', 'surname', 'name', 'lastname', 'password1', 'password2', 'is_superuser', 'is_staff', 'is_active', 'is_teacher', 'is_student', )}
        ),
    )

    # поиск по полям
    search_fields = ('email', 'surname', 'name', 'lastname', )

    # сортировка списка по полям
    ordering = ('email', 'surname', 'name', 'lastname', )

# class Student_Admin(UserAdmin):
#     # add_form = StudentCreationForm
#     # form = StudentChangeForm
#     model = Student

#     # список юзеров в админке
#     list_display = ('email', 'surname', 'name', 'lastname', 'group', 'is_staff', 'is_active', 'is_superuser', )

#     # фильтр в админке
#     list_filter = ('is_staff', 'is_active', 'is_superuser', )

#     # просмотр и изменение полей
#     fieldsets = (
#         (None, {'fields': ('email', 'surname', 'name', 'lastname', 'group', 'password', 'date_joined', 'date_registration', )}),
#         ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser', )}),
#     )

#     # поля при добавлении в админке
#     add_fieldsets = (
#         (None, {
#             'classes': ('wide', ),
#             'fields': ('email', 'surname', 'name', 'lastname', 'group', 'password1', 'password2', 'is_staff', 'is_active', 'is_superuser', )}
#         ),
#     )

#     # поиск по полям
#     search_fields = ('email', 'surname', 'name', 'lastname', 'group__name', )

#     # сортировка списка по полям
#     ordering = ('email', 'surname', 'name', 'lastname', 'group', )

# # STR-module admin:
# class Teacher_Admin(admin.ModelAdmin):
#     model = Teacher
#     list_display = ('email', 'surname', 'name', 'lastname', )
#     search_fields = ('email', 'surname', 'name', 'lastname', )
#     ordering = ('email', 'surname', 'name', 'lastname', )


class Criterion_Admin(admin.ModelAdmin):
    model = Criterion
    list_display = ('name', )
    search_fields = ('name', )
    ordering = ('name', )


class Group_Admin(admin.ModelAdmin):
    model = Group
    list_display = ('name', 'education_form')
    search_fields = ('name', 'education_form')
    ordering = ('name', 'education_form')


class Subject_Admin(admin.ModelAdmin):
    model = Subject
    form = SubjectForm
    list_display = ('name', )
    search_fields = ('name', )
    ordering = ('name', )


class Subject_Group_Admin(admin.ModelAdmin):
    model = Subject_Group
    list_display = ('id', 'group', 'semester', 'subject', )
    search_fields = ('semester', 'group__name', 'subject__type', 'subject__name', 'id', )
    ordering = ('id', 'group', 'semester', 'subject', )


class Teacher_Subject_Admin(admin.ModelAdmin):
    model = Teacher_Subject
    list_display = ('id', 'teacher', 'subject', )
    search_fields = ('teacher__email', 'teacher__surname', 'teacher__name', 'teacher__lastname', 'subject__type', 'subject__name', 'id', )
    ordering = ('id', 'teacher', 'subject', )


class Grade_Admin(admin.ModelAdmin):
    model = Grade
    list_display = ('id', 'student', 'teacher_subject', 'criterion', 'grade', )
    search_fields = ('student__email', 'student__surname', 'student__name', 'student__lastname', 'criterion__name', 'teacher_subject__subject__type', 'teacher_subject__subject__name', 'teacher_subject__teacher__email', 'teacher_subject__teacher__surname', 'teacher_subject__teacher__name', 'teacher_subject__teacher__lastname', 'grade', 'id', )
    ordering = ('id', 'student', 'teacher_subject', 'criterion', 'grade', )

# Schedule-module admin:
class Campus_Admin(admin.ModelAdmin):
    model = Campus
    list_display = ('campus_name', 'address')
    search_fields = ('campus_name', 'address')
    ordering = ('campus_name', 'address')

class Audience_Admin(admin.ModelAdmin):
    model = Audience
    list_display = ('audience_number', 'campus', 'audience_type', 'capacity')
    search_fields = ('audience_number', 'campus', 'audience_type', 'capacity')
    ordering = ('audience_number', 'campus', 'audience_type', 'capacity')

class Schedule_Admin(admin.ModelAdmin):
    model = Schedule
    list_display = ('subject', 'subject_type', 'audience', 'group', 'time_range', 'weekday', 'even_week', 'subgroup_number', 'teacher', 'semester_year')
    search_fields = ('subject', 'subject_type', 'audience', 'group', 'time_range', 'weekday', 'even_week', 'subgroup_number', 'teacher', 'semester_year')
    ordering = ('subject', 'subject_type', 'audience', 'group', 'time_range', 'weekday', 'even_week', 'subgroup_number', 'teacher', 'semester_year')


# Attendance-module admin:
class Attendance_Admin(admin.ModelAdmin):
    model = Attendance
    list_display = ('subject', 'subject_date', 'student', 'attended')
    search_fields = ('subject', 'subject_date', 'student', 'attended')
    ordering = ('subject', 'subject_date', 'student', 'attended')

admin.site.unregister(mod.Group)

admin.site.register(User, User_Admin)

admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Criterion, Criterion_Admin)
admin.site.register(Group, Group_Admin)
admin.site.register(Subject, Subject_Admin)

admin.site.register(Subject_Group, Subject_Group_Admin)
admin.site.register(Teacher_Subject, Teacher_Subject_Admin)
admin.site.register(Grade, Grade_Admin)

admin.site.register(Campus, Campus_Admin)
admin.site.register(Audience, Audience_Admin)
admin.site.register(Schedule, Schedule_Admin)

admin.site.register(Attendance, Attendance_Admin)