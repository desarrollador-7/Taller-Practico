import re
from django import forms
from django.core.exceptions import ValidationError
from .models import *
from django.utils import timezone
from .models import Licencia
from .models import Propietario

class PropietarioForm(forms.ModelForm):
    telefono = forms.CharField(required=False, label='Telefono*', max_length=20)
    class Meta:
        model = Propietario
        fields = ['dni','placa','nombre','apellido','direccion','telefono','email']
        
    def clean_dni(self):
        dni = self.cleaned_data.get('dni') 
        # Validar unicidad
        if self.instance.pk:  # Si estamos editando
            if Propietario.objects.filter(dni=dni).exclude(pk=self.instance.pk).exists():
                raise ValidationError('Ya existe un Propietario registrado con este DNI')
        else:  # Si estamos creando
            if Propietario.objects.filter(dni=dni).exists():
                raise ValidationError('Ya existe un Propietario registrado con este DNI')
        
        return dni
    
    
    def clean_telefono(self):
        telefono = self.cleaned_data.get('telefono')
        if telefono and len(telefono) > 10:
            raise forms.ValidationError('El número de teléfono no debe tener más de 10 dígitos')
        if telefono and len(telefono) < 10:
            raise forms.ValidationError('El número de teléfono no debe tener menos de 10 dígitos')
        return telefono
    
    
    # def clean_email(self):
    #     email = forms.EmailField(required=False, label='Email*')
    #     email = self.cleaned_data.get('email')
    
    #     # Validar formato de correo electrónico
    #     patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    #     if not re.match(patron, email):
    #         raise forms.ValidationError('Ingresa un correo electrónico válido: "ejemplo@gmail.com"')
    
    #     return email


class LicenciaForm(forms.ModelForm): 
    class Meta:
        model = Licencia
        fields = ['numero','dni','tipo','fecha_emision','fecha_vencimiento','estado']
        widgets = {
            'fecha_emision': forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
            'fecha_vencimiento': forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
        }
    
    def clean_numero(self):
        numero = self.cleaned_data.get('numero') 
        # Validar unicidad
        if self.instance.pk:  # Si estamos editando
            if Licencia.objects.filter(numero=numero).exclude(pk=self.instance.pk).exists():
                raise ValidationError('Ya existe una Licencia registrado con esta numero')
        else:  # Si estamos creando
            if Licencia.objects.filter(numero=numero).exists():
                raise ValidationError('Ya existe una Licencia registrado con esta numero')
        
        return numero
    
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