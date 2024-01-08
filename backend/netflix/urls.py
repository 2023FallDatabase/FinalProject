from django.urls import path
from . import views

urlpatterns = [
    # TODO: Delete them.
    path('', views.main, name='main'),
    path('members/', views.members, name='members'),
    path('forms/', views.forms, name='forms'),
    path('members/details/<int:id>', views.details, name='details'),
    path('update/<int:id>', views.update, name='update'),
    path('delete/<int:id>', views.delete, name='delete')
]  