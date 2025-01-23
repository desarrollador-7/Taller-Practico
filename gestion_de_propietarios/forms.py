import re
from django import forms
from django.core.exceptions import ValidationError
from .models import *
from django.utils import timezone

# def clean_telefono(self):
    #     telefono = self.cleaned_data.get('telefono')
        
    #     if telefono > 10:
    #         raise ValidationError('El número no debe tener más de 10 dígitos')
    #     return telefono

class PropietarioForm(forms.ModelForm):
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
    
    # def clean_dni(self):
    #     dni = self.cleaned_data.get('dni')
        
    #     if dni == dni:
    #         raise ValidationError('El numero de licencia es irrepetible.')
    #     return dni
    
    def clean_fecha_emision(self):
        fecha_emision = self.cleaned_data.get('fecha_emision')
        fecha_actual = timezone.now().date()
    
        if fecha_emision:
            fecha_emision = fecha_emision.date() if hasattr(fecha_emision, 'date') else fecha_emision
            
            if fecha_emision < fecha_actual:
                raise ValidationError('La fecha de emisión no puede ser menor a la fecha actual')
    
        return fecha_emision

    def clean_fecha_vencimiento(self):
        fecha_vencimiento = self.cleaned_data.get('fecha_vencimiento')
        fecha_emision = self.cleaned_data.get('fecha_emision')
        
        if fecha_vencimiento and fecha_emision:
            fecha_vencimiento = fecha_vencimiento.date() if hasattr(fecha_vencimiento, 'date') else fecha_vencimiento
            fecha_emision = fecha_emision.date() if hasattr(fecha_emision, 'date') else fecha_emision
        
            if fecha_vencimiento < fecha_emision:
                raise ValidationError('La fecha de vencimiento no puede ser menor a la fecha de emisión')
    
        return fecha_vencimiento