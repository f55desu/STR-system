from django.urls import path

from .views import APIAttendance, APISchedule
from . import views

urlpatterns = [
    path('', views.registration, name='registration'),
    path('home', views.home, name='home'),
    path('str', views.str, name='str'),
    path('acc_active_sent', views.acc_active_sent, name='acc_active_sent'),
    path('acc_active_confirmed', views.acc_active_confirmed, name='acc_active_confirmed'),
    path('activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', views.activate, name='activate'),
    path('api/v1/attendance_list', APIAttendance.as_view()),
    path('api/v1/schedule_list', APISchedule.as_view()),
]