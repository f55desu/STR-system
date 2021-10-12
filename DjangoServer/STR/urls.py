from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('rating', views.rating, name='rating'),
    path('registration', views.registration, name='registration'),
]