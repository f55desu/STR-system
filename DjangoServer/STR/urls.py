from django.urls import path
from . import views

urlpatterns = [
    path('', views.registration, name='registration'),
    path('rating', views.rating, name='rating'),
    path('home', views.home, name='home'),
    path('acc_active_sent', views.acc_active_sent, name='acc_active_sent'),
    path('acc_active_confirmed', views.acc_active_confirmed, name='acc_active_confirmed'),
    path('activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', views.activate, name='activate'),
]