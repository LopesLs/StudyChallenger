from django import forms

from .models import Apostila

class ApostilaForm(forms.ModelForm):
    class Meta:
        model = Apostila
        fields = ['titulo', 'arquivo']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'arquivo': forms.FileInput(attrs={'class': 'form-control'}),
        }