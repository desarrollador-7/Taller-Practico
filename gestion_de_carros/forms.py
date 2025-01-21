import re
from django import forms
from django.core.exceptions import ValidationError
from .models import Carro
from datetime import datetime


class CarroForm(forms.ModelForm): 
    class Meta:
        model = Carro
        fields = ['placa','marca','modelo','anio','color','tipo','precio','kilometraje','disponible']
        widgets = {
            'anio': forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
        }
        
    def clean_placa(self):
        placa = self.cleaned_data.get('placa')
        
        # Validar formato
        if not re.match(r'^[A-Z]{3}-\d{3}$', placa):
            raise ValidationError('El formato de la placa debe ser ABC-123')
        
        # Validar unicidad
        if self.instance.pk:  # Si estamos editando
            if Carro.objects.filter(placa=placa).exclude(pk=self.instance.pk).exists():
                raise ValidationError('Ya existe un carro registrado con esta placa')
        else:  # Si estamos creando
            if Carro.objects.filter(placa=placa).exists():
                raise ValidationError('Ya existe un carro registrado con esta placa')
        
        return placa
    
    def clean_kilometraje(self):
        kilometraje = self.cleaned_data.get('kilometraje')
    
        # Validar que el kilometraje sea positivo
        if kilometraje and kilometraje < 0:
            raise ValidationError('El kilometraje no puede ser negativo')
        return kilometraje

    def clean_precio(self):
        precio = self.cleaned_data.get('precio')
        
        # Validar que el precio sea positivo
        if precio and precio <= 0:
            raise ValidationError('El precio debe ser mayor a 0')
        return precio

    def clean_anio(self):
        anio = self.cleaned_data.get('anio')
        
        if anio:
            fecha_actual = datetime.now().date()  # Convertimos a date()
            anio_fecha = anio.date() if isinstance(anio, datetime) else anio  # Convertimos anio a date si es datetime
            
            if anio_fecha > fecha_actual:
                raise ValidationError('La fecha no puede ser mayor a la fecha actual')
        return anio

    def clean_marca(self):
        marca = self.cleaned_data.get('marca')
        
        # Validar que marca no esté vacío
        if not marca or marca.strip() == '':
            raise ValidationError('El campo marca es obligatorio')
        return marca.strip()

    def clean_modelo(self):
        modelo = self.cleaned_data.get('modelo')
        
        # Validar que modelo no esté vacío
        if not modelo or modelo.strip() == '':
            raise ValidationError('El campo modelo es obligatorio')
        return modelo.strip()
    
    
    

