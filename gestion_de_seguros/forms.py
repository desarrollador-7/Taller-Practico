from django import forms
from .models import *


class AseguradoraForm(forms.ModelForm):
    class Meta:
        model = Aseguradora
        fields = ['id_aseguradora','nombre','direccion','telefono','email']


class SeguroForm(forms.ModelForm):
    class Meta:
        model = Seguro
        fields = ['dni','placa','id_aseguradora','fecha_inicio','fecha_fin','costo','tipo_cobertura','estado']
        widgets = {
            'fecha_inicio': forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
            'fecha_fin': forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
        }