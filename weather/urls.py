
from unicodedata import name
from django.urls import path
from .import views

urlpatterns = [
    path('weather/', views.index, name='weather'),
    path('delete/<city_name>', views.delete_city, name='delete_city')
]