from django.urls import path
from . import views

urlpatterns = [
    path('api/AllCountry/', views.AllCountry, name='AllCountry'),
    path('api/OneCountry/<slug:show_id>', views.OneCountry, name='OneCountry'),
    path('api/AllCast/', views.AllCast, name='AllCast'),
    path('api/OneCast/<int:id>', views.OneCast, name='OneCast'),
    path('api/AllForm/', views.AllForm, name='AllForm'),
    path('api/AllForm/<slug:show_id>', views.AllFormFilter, name='AllFormFilter'),
    path('api/OneForm/<slug:show_id>', views.OneForm, name='OneForm'),
    path('api/AllComment/<slug:show_id>', views.AllComment, name='AllComment'),
    path('api/OneComment/<int:id>', views.OneComment, name='OneComment'),
    path('api/AllRanking/', views.AllRanking, name='OneComment'),
    path('api/Filter/', views.Filter, name='filter'),
    
]  