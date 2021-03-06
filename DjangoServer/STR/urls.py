from django.urls import path, include

from .views import APIAttendance, APISchedule
from . import views

urlpatterns = [
    path('', views.registration, name='registration'),
    path('home', views.home, name='home'),
    path('str', views.str, name='str'),
    path('acc_active_sent', views.acc_active_sent, name='acc_active_sent'),
    path('acc_active_confirmed', views.acc_active_confirmed, name='acc_active_confirmed'),
    path('activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', views.activate, name='activate'),
    path('api/v1/auth/', include('rest_framework.urls')),
    path('api/v1/attendance_list', views.auth_check),
    path('api/v1/schedule_list', views.auth_check),
]   