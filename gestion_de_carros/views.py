from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import *
from .forms import *
from django.contrib.auth.mixins import PermissionRequiredMixin


class ListaCarro(ListView):
    
    """Clase para la lista de un objeto
    """    
    
    model = Carro
    template_name = 'listado_carros.html'
    context_object_name = 'carros' 
    

class VistaCarro(DetailView):
    
    """Clase para la vista de un objeto
    """    
    
    model = Carro
    template_name = 'vista_carro.html'
    success_url = reverse_lazy('carros')
    
class CrearCarro(CreateView):
    
    """Clase para la creacion de un objeto
    """    
    
    model = Carro
    form_class = CarroForm
    template_name = 'crear_carro.html'
    success_url = reverse_lazy('listado_carros')
    
class ActualizarCarro(UpdateView):
    
    """Clase para la edicion de un objeto
    """    
    
    model = Carro
    form_class = CarroForm
    template_name= 'crear_carro.html'
    success_url = reverse_lazy('listado_carros')
    
    
class EliminarCarro(DeleteView):
    
    """Clase para la eliminacion de un objeto
    """    
    
    model = Carro
    template_name = 'eliminar_carro.html'
    success_url = reverse_lazy('listado_carros')