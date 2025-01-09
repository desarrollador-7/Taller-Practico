from django import forms
from .models import *



class CarroForm(forms.ModelForm):
    class Meta:
        model = Carro
        fields = ['placa','marca','modelo','anio','color','tipo','precio','kilometraje','disponible']
        widgets = {
            'anio': forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
        }