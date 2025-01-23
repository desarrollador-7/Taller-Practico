from django import forms
from django.core.exceptions import ValidationError
from .models import Multas
from datetime import datetime



class MultasForm(forms.ModelForm):
    #Cometarios del código
    class Meta:
        model = Multas
        fields = ['dni','placa','fecha','infraccion','monto','estado']
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
        }
    
    
    def clean_fecha(self):
        fecha = self.cleaned_data.get('fecha')
        
        if fecha:
            fecha_actual = datetime.now().date()  # Convertimos a date()
            anio_fecha = fecha.date() if isinstance(fecha, datetime) else fecha  # Convertimos anio a date si es datetime
            
            if anio_fecha < fecha_actual:
                raise ValidationError('La fecha no puede ser mayor a la fecha actual')
        return fecha
    
    
    def clean_monto(self):
        monto = self.cleaned_data.get('monto')
        
        # Validar que el precio sea positivo
        if monto and monto <= 100.000:
            raise ValidationError('El monto debe ser mayor a 100.000 mil')
        return monto