from django import forms
from .models import *
from .models import Taller
from django.core.exceptions import ValidationError
from django.utils import timezone


class TallerForm(forms.ModelForm):
    class Meta:
        model = Taller
        fields = ['idn','nombre','direccion','telefono','especializacion']
    
    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre') 
        # Validar unicidad
        if self.instance.pk:  # Si estamos editando
            if Taller.objects.filter(nombre=nombre).exclude(pk=self.instance.pk).exists():
                raise ValidationError('Ya existe un Taller registrado con esta nombre')
        else:  # Si estamos creando
            if Taller.objects.filter(nombre=nombre).exists():
                raise ValidationError('Ya existe un Taller registrado con esta nombre')
        return nombre
    
    
    def clean_telefono(self):
        telefono = self.cleaned_data.get('telefono')
        if telefono and len(telefono) > 10:
            raise forms.ValidationError('El número de teléfono no debe tener más de 10 dígitos')
        if telefono and len(telefono) < 10:
            raise forms.ValidationError('El número de teléfono no debe tener menos de 10 dígitos')
        return telefono


class MantenimientoForm(forms.ModelForm):
    class Meta:
        model = Mantenimiento
        fields = ['idn','placa','id_taller','fecha','tipo_servicio','costo','descripcion','estado']
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
        }
    
    
    def clean_fecha(self):
        fecha = self.cleaned_data.get('fecha')
        fecha_actual = timezone.now().date()
    
        if fecha:
            fecha = fecha.date() if hasattr(fecha, 'date') else fecha
            
            if fecha < fecha_actual:
                raise ValidationError('La fecha de inicio no puede ser menor a la fecha actual')
    
        return fecha