from django import forms
from django.core.exceptions import ValidationError
from .models import Carro
import datetime


class CarroForm(forms.ModelForm): 
    class Meta:
        model = Carro
        fields = ['placa','marca','modelo','anio','color','tipo','precio','kilometraje','disponible']
        widgets = {
            'anio': forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
        }
        
    # def clean_anio(self):
    #     anio = self.cleaned_data.get('anio')
    #     if anio.year > datetime.now().year:
    #         raise ValidationError("El año no puede ser mayor que el año actual.")
    #     return anio

