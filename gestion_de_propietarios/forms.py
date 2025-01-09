from django import forms
from .models import *



class PropietarioForm(forms.ModelForm):
    #Cometarios del código
    class Meta:
        model = Propietario
        fields = ['dni','placa','nombre','apellido','direccion','telefono','email']