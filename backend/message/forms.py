from django import forms
from .models import UserMessage


class UserMessageForm(forms.ModelForm):
    class Meta:
        model = UserMessage
        fields = ['show_id', 'name', 'message', 'rating']
