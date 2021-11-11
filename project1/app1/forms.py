from django import forms
from .models import Instagram

class InstagramForm(forms.ModelForm):
    class Meta:
        model=Instagram
        fields='__all__'