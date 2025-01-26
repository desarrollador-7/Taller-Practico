from django import forms
from .models import *
from .models import Aseguradora
from django.core.exceptions import ValidationError
from django.utils import timezone


class AseguradoraForm(forms.ModelForm):
    class Meta:
        model = Aseguradora
        fields = ['id_aseguradora','nombre','direccion','telefono','email']
        
    
    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre') 
        # Validar unicidad
        if self.instance.pk:  # Si estamos editando
            if Aseguradora.objects.filter(nombre=nombre).exclude(pk=self.instance.pk).exists():
                raise ValidationError('Ya existe una Aseguradora registrado con esta nombre')
        else:  # Si estamos creando
            if Aseguradora.objects.filter(nombre=nombre).exists():
                raise ValidationError('Ya existe una Aseguradora registrado con esta nombre')
        return nombre
            
            
    def clean_telefono(self):
        telefono = self.cleaned_data.get('telefono')
        if telefono and len(telefono) > 10:
            raise forms.ValidationError('El número de teléfono no debe tener más de 10 dígitos')
        if telefono and len(telefono) < 10:
            raise forms.ValidationError('El número de teléfono no debe tener menos de 10 dígitos')
        return telefono


class SeguroForm(forms.ModelForm):
    class Meta:
        model = Seguro
        fields = ['dni','placa','id_aseguradora','fecha_inicio','fecha_fin','costo','tipo_cobertura','estado']
        widgets = {
            'fecha_inicio': forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
            'fecha_fin': forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
        }
    
    def clean_fecha_inicio(self):
        fecha_inicio = self.cleaned_data.get('fecha_inicio')
        fecha_actual = timezone.now().date()
    
        if fecha_inicio:
            fecha_inicio = fecha_inicio.date() if hasattr(fecha_inicio, 'date') else fecha_inicio
            
            if fecha_inicio < fecha_actual:
                raise ValidationError('La fecha de inicio no puede ser menor a la fecha actual')
    
        return fecha_inicio

    def clean_fecha_fin(self):
        fecha_fin = self.cleaned_data.get('fecha_fin')
        fecha_inicio = self.cleaned_data.get('fecha_inicio')
        
        if fecha_fin and fecha_inicio:
            fecha_fin = fecha_fin.date() if hasattr(fecha_fin, 'date') else fecha_fin
            fecha_inicio = fecha_inicio.date() if hasattr(fecha_inicio, 'date') else fecha_inicio
        
            if fecha_fin < fecha_inicio:
                raise ValidationError('La fecha de fin no puede ser menor a la fecha de inicio')
    
        return fecha_fin