from django import forms
from .models import *

class form_model_form(forms.ModelForm):
    class Meta:
        model=Form
        fields='__all__'
        widgets = {
            'show_id': forms.TextInput(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'type': forms.TextInput(attrs={'class': 'form-control'}),
            'director':forms.TextInput(attrs={'class': 'form-control'}),
            'country': forms.TextInput(attrs={'class': 'form-control'}),
            'rating': forms.TextInput(attrs={'class': 'form-control'}),
            'duration': forms.TextInput(attrs={'class': 'form-control'}),
            'release_year': forms.TextInput(attrs={'class': 'form-control'}),
            'catalog': forms.TextInput(attrs={'class': 'form-control'}),
            'average_score': forms.TextInput(attrs={'class': 'form-control'}),
            'score_count': forms.TextInput(attrs={'class': 'form-control'}),
            'comments': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'show_id': '電影編號',
            'title': '電影名字',
            'type': '影集類別',
            'director': '導演',
            'country': '國家名字',
            'rating': '電影分級',
            'duration': '時長',
            'release_year': '年分',
            'catalog': '類別',
            'average_score': '平均分數',
            'score_count': '評分次數',
            'comments': '留言'
            
        }


