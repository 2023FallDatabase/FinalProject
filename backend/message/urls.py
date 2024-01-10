from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.submitform, name='formUrl'),
    path('showform/', views.showform, name='showformUrl'),
]
