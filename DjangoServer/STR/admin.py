from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import *


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser

    # список юзеров в админке
    list_display = ('email', 'surname', 'name', 'lastname', 'is_staff', 'is_active', 'is_superuser',)

    # фильтр в админке
    list_filter = ('is_staff', 'is_active', 'is_superuser',)

    # просмотр и изменение полей
    fieldsets = (
        (None, {'fields': ('email', 'surname', 'name', 'lastname', 'password')}),
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
    ordering = ('email',)


admin.site.register(CustomUser, CustomUserAdmin)

# Register your models here.
admin.site.register(Subject)
# admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Ticket)
admin.site.register(Mark)
admin.site.register(Data)
