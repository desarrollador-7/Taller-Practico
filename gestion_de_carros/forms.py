from django import forms
from .models import *



class CarroForm(forms.ModelForm):
    class Meta:
        model = Carro
        fields = ['marca','modelo','anio','precio','disponible']
        widgets = {
            'anio': forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
        }