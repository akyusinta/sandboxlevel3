from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('entries/', views.index, name = 'entries'),
    path('add/', views.add, name = 'add')
]
