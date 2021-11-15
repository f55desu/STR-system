from django.contrib.auth.admin import UserAdmin
from django.contrib import admin

from django.forms import *

from .forms import *
from .models import *


class StudentAdmin(UserAdmin):
    add_form = StudentCreationForm
    form = StudentChangeForm
    model = Student

    # список юзеров в админке
    list_display = ('id', 'email', 'surname', 'name', 'lastname', 'is_staff', 'is_active', 'is_superuser', )

    # фильтр в админке
    list_filter = ('is_staff', 'is_active', 'is_superuser',)

    # просмотр и изменение полей
    fieldsets = (
        (None, {'fields': ('email', 'surname', 'name', 'lastname', 'password', 'date_joined', 'date_registration', )}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser',)}),
    )

    # поля при добавлении в админке
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'surname', 'name', 'lastname', 'password1', 'password2', 'is_staff', 'is_active', 'is_superuser')}
        ),
    )

    # поиск по полям
    search_fields = ('email', 'surname', 'name', 'lastname')

    # сортировка списка по полям
    ordering = ('id',)


class TeacherAdmin(admin.ModelAdmin):
    model = Teacher
    list_display = ('id', 'surname', 'name', 'lastname', 'email', )
    search_fields = ('id', 'surname', 'name', 'lastname', 'email',)
    ordering = ('id', )


class CriterionAdmin(admin.ModelAdmin):
    model = Criterion
    list_display = ('id', 'name', )
    search_fields = ('id', 'name', )
    ordering = ('id', )


class GroupAdmin(admin.ModelAdmin):
    model = Group
    list_display = ('id', 'name', )
    search_fields = ('id', 'name', )
    ordering = ('id', )


class SubjectAdmin(admin.ModelAdmin):
    model = Subject
    form = SubjectForm
    list_display = ('id', 'name', 'type', )
    search_fields = ('id', 'name', 'type', )
    ordering = ('id', )

    # def save_model(self, request, obj, form, change):
    #     obj.user = request.user
    #     super(temp_mainAdmin, self).save_model(request, obj, form, change)

    # def changeform_view(self, request, obj_id, form_url, extra_context=None):

    #     l_mod = temp_main.objects.latest('id')

    #     extra_context = {
    #         'lmod': l_mod,
    #     }
    #     return super(temp_mainAdmin, self).changeform_view(request, obj_id, form_url, extra_context=extra_context)

    # def get_form(self, request, obj=None, **kwargs):
    #     form = super(SubjectAdmin, self).get_form(request, obj, **kwargs)
    #     # ) SelectMultiple(choices=(
    #     #     (1, 'Лекция'),
    #     #     (2, 'Практика'),
    #     # ))
    #     form.base_fields['type'].widget = Select(
    #         'Лекция',
    #         'Практика',
    #         )

    #     return form

admin.site.register(Student, StudentAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Criterion, CriterionAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(Subject, SubjectAdmin)


admin.site.register(StudentGroup)
admin.site.register(SubjectGroup)
admin.site.register(TeacherSubject)
admin.site.register(SubjectStudentCriterionMark)