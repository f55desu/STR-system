from django.urls import path
from . import views

urlpatterns = [
    path('', views.registration, name='registration'),
    path('rating', views.rating, name='rating'),
    path('home', views.home, name='home'),
]