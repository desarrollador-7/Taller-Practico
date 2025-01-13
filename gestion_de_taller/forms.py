from django import forms
from .models import *


class TallerForm(forms.ModelForm):
    class Meta:
        model = Taller
        fields = ['idn','nombre','direccion','telefono','especializacion']


class MantenimientoForm(forms.ModelForm):
    class Meta:
        model = Mantenimiento
        fields = ['idn','placa','id_taller','fecha','tipo_servicio','costo','descripcion','estado']
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
        }