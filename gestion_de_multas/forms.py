from django import forms
from .models import *



class MultasForm(forms.ModelForm):
    #Cometarios del código
    class Meta:
        model = Multas
        fields = ['dni','placa','fecha','infraccion','monto','estado']
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
        }