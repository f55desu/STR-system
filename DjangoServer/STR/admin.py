from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Subject)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Ticket)
admin.site.register(Mark)
admin.site.register(Data)