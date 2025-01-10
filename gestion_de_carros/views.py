from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import *
from .forms import *
from django.contrib.auth.mixins import PermissionRequiredMixin


class ListaCarro(ListView):
    """_summary_

    :param ListView: _description_
    :type ListView: _type_
    """       
        
    model = Carro
    template_name = 'listado_carros.html'
    context_object_name = 'carros' 
    

class VistaCarro(DetailView):
    """_summary_

    :param DetailView: _description_
    :type DetailView: _type_
    """    

    model = Carro
    template_name = 'vista_carro.html'
    success_url = reverse_lazy('carros')
    
class CrearCarro(CreateView):
    """_summary_

    :param CreateView: _description_
    :type CreateView: _type_
    """    
    
    model = Carro
    form_class = CarroForm
    template_name = 'crear_carro.html'
    success_url = reverse_lazy('listado_carros')
    
class ActualizarCarro(UpdateView):
    """_summary_

    :param UpdateView: _description_
    :type UpdateView: _type_
    """       
    
    model = Carro
    form_class = CarroForm
    template_name= 'crear_carro.html'
    success_url = reverse_lazy('listado_carros')
    
    
class EliminarCarro(DeleteView):
    """_summary_

    :param DeleteView: _description_
    :type DeleteView: _type_
    """       
    
    model = Carro
    template_name = 'eliminar_carro.html'
    success_url = reverse_lazy('listado_carros')