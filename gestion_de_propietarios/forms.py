from django import forms
from .models import *



class PropietarioForm(forms.ModelForm):
    #Cometarios del código
    class Meta:
        model = Propietario
        fields = ['dni','placa','nombre','apellido','direccion','telefono','email']

class LicenciaForm(forms.ModelForm): 
    class Meta:
        model = Licencia
        fields = ['numero','dni','tipo','fecha_emision','fecha_vencimiento','estado']
        widgets = {
            'fecha_emision': forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
            'fecha_vencimiento': forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
        }